#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

###############################################################################
#                                                                             #
# Copyright (c) 2018 Idiap Research Institute, http://www.idiap.ch/           #
# Contact: beat.support@idiap.ch                                              #
#                                                                             #
# This file is part of the beat.backend.python module of the BEAT platform.   #
#                                                                             #
# Commercial License Usage                                                    #
# Licensees holding valid commercial BEAT licenses may use this file in       #
# accordance with the terms contained in a written agreement between you      #
# and Idiap. For further information contact tto@idiap.ch                     #
#                                                                             #
# Alternatively, this file may be used under the terms of the GNU Affero      #
# Public License version 3 as published by the Free Software and appearing    #
# in the file LICENSE.AGPL included in the packaging of this file.            #
# The BEAT platform is distributed in the hope that it will be useful, but    #
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY  #
# or FITNESS FOR A PARTICULAR PURPOSE.                                        #
#                                                                             #
# You should have received a copy of the GNU Affero Public License along      #
# with the BEAT platform. If not, see http://www.gnu.org/licenses/.           #
#                                                                             #
###############################################################################


"""Executes a loop algorithm. (%(version)s)

usage:
  %(prog)s [--debug] <addr> <dir> <cache> [<db_addr>]
  %(prog)s (--help)
  %(prog)s (--version)


arguments:
  <addr>    Listen for incoming request on this address ('host:port')
  <dir>     Directory containing all configuration required to run the views
  <cache>   Path to the cache
  <db_addr> Address for databases-related I/O requests


options:
  -h, --help         Shows this help message and exit
  -V, --version      Shows program's version number and exit
  -d, --debug        Runs executor in debugging mode

"""

import logging

import os
import sys
import docopt
import simplejson
import pwd
import stat

import zmq

from beat.backend.python.execution import LoopExecutor
from beat.backend.python.execution import LoopMessageHandler
from beat.backend.python.exceptions import UserError


#----------------------------------------------------------


def process_traceback(tb, prefix):
    import traceback

    algorithms_prefix = os.path.join(prefix, 'algorithms') + os.sep

    for first_line, line in enumerate(tb):
        if line[0].startswith(algorithms_prefix):
            break

    s = ''.join(traceback.format_list(tb[first_line:]))
    s = s.replace(algorithms_prefix, '').strip()

    return s


#----------------------------------------------------------


def main(arguments=None):

    # Parse the command-line arguments
    if arguments is None:
        arguments = sys.argv[1:]

    package = __name__.rsplit('.', 2)[0]
    version = package + ' v' + \
              __import__('pkg_resources').require(package)[0].version

    prog = os.path.basename(sys.argv[0])

    args = docopt.docopt(
        __doc__ % dict(prog=prog, version=version),
        argv=arguments,
        version=version
    )


    # Setup the logging system
    formatter = logging.Formatter(fmt="[%(asctime)s - loop_provider.py - " \
                                      "%(name)s] %(levelname)s: %(message)s",
                                  datefmt="%d/%b/%Y %H:%M:%S")

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    root_logger = logging.getLogger('beat.backend.python')
    root_logger.addHandler(handler)

    if args['--debug']:
        root_logger.setLevel(logging.DEBUG)
    else:
        root_logger.setLevel(logging.INFO)

    logger = logging.getLogger(__name__)


    # Create the message handler
    message_handler = LoopMessageHandler(args['<addr>'])

    context = None
    db_socket = None
    if args['<db_addr>']:
        context = zmq.Context()
        db_socket = context.socket(zmq.PAIR)
        db_socket.connect(args['<db_addr>'])
        logger.debug("loop: zmq client connected to db `%s'", args['<db_addr>'])


    # If necessary, change to another user (with less privileges, but has access
    # to the databases)
    with open(os.path.join(args['<dir>'], 'configuration.json'), 'r') as f:
        cfg = simplejson.load(f)

    try:

        # Check the dir
        if not os.path.exists(args['<dir>']):
            raise IOError("Running directory `%s' not found" % args['<dir>'])

        # Sets up the execution
        try:
            loop_executor = LoopExecutor(message_handler=message_handler,
                                         directory=args['<dir>'],
                                         cache_root=args['<cache>'],
                                         db_socket=db_socket)
        except (MemoryError):
            raise
        except Exception as e:
            import traceback
            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb = traceback.extract_tb(exc_traceback)
            s = process_traceback(tb, os.path.join(args['<dir>'], 'prefix'))
            raise UserError("%s%s: %s" % (s, type(e).__name__, e))

        try:
            status = loop_executor.setup()
            if not status:
                raise UserError("Could not setup loop algorithm (returned False)")
        except (UserError, MemoryError):
            raise
        except Exception as e:
            import traceback
            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb = traceback.extract_tb(exc_traceback)
            s = process_traceback(tb, loop_executor.prefix)
            raise UserError("%s%s: %s" % (s, type(e).__name__, e))

        # Prepare the algorithm
        try:
            status = loop_executor.prepare()
            if not status:
                raise UserError("Could not prepare loop algorithm (returned False)")
        except (UserError, MemoryError):
            raise
        except Exception as e:
            import traceback
            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb = traceback.extract_tb(exc_traceback)
            s = process_traceback(tb, loop_executor.prefix)
            raise UserError("%s%s: %s" % (s, type(e).__name__, e))

        # Execute the code
        try:
            logger.debug("loop: Starting process")
            loop_executor.process()
            loop_executor.wait()
        except (MemoryError):
            raise
        except Exception as e:
            import traceback
            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb = traceback.extract_tb(exc_traceback)
            s = process_traceback(tb, os.path.join(args['<dir>'], 'prefix'))
            raise UserError("%s%s: %s" % (s, type(e).__name__, e))

    except UserError as e:
        message_handler.send_error(str(e), 'usr')
        message_handler.destroy()
        return 1

    except MemoryError as e:
        # Say something meaningful to the user
        msg = "The user process for this block ran out of memory. We " \
              "suggest you optimise your code to reduce memory usage or, " \
              "if this is not an option, choose an appropriate processing " \
              "queue with enough memory."
        message_handler.send_error(msg, 'usr')
        message_handler.destroy()
        return 1

    except Exception as e:
        import traceback
        message_handler.send_error(traceback.format_exc(), 'sys')
        message_handler.destroy()
        return 1

    if db_socket is not None:
        db_socket.setsockopt(zmq.LINGER, 0)
        db_socket.close()

        context.term()
        logger.debug("loop: 0MQ client finished")

    message_handler.destroy()

    return 0



if __name__ == '__main__':
    sys.exit(main())

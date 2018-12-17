#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

###############################################################################
#                                                                             #
# Copyright (c) 2016 Idiap Research Institute, http://www.idiap.ch/           #
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


"""Executes a single algorithm. (%(version)s)

usage:
  %(prog)s [--debug] [--cache=<path>] <addr> <dir> [<db_addr>] [<loop_addr>]
  %(prog)s (--help)
  %(prog)s (--version)


arguments:
  <addr>      Address of the controlling process
  <dir>       Directory containing all configuration required to run the user
              algorithm
  <db_addr>   Address for databases-related I/O requests
  <loop_addr> Address for loop-related I/O requests


options:
  -h, --help         Shows this help message and exit
  -V, --version      Shows program's version number and exit
  -d, --debug        Runs executor in debugging mode
  -c, --cache=<path> Cache prefix, otherwise defaults to '/cache'

"""

import logging

import os
import sys
import docopt
import pwd
import stat
import simplejson
import subprocess

import zmq

from beat.backend.python.execution import AlgorithmExecutor
from beat.backend.python.exceptions import UserError


#----------------------------------------------------------


def send_error(logger, socket, tp, message):
    """Sends a user (usr) or system (sys) error message to the infrastructure"""

    logger.debug('send: (err) error')
    socket.send_string('err', zmq.SNDMORE)
    socket.send_string(tp, zmq.SNDMORE)
    logger.debug('send: """%s"""' % message.rstrip())
    socket.send_string(message)

    poller = zmq.Poller()
    poller.register(socket, zmq.POLLIN)

    this_try = 1
    max_tries = 5
    timeout = 1000 #ms
    while this_try <= max_tries:
        socks = dict(poller.poll(timeout)) #blocks here, for 5 seconds at most
        if socket in socks and socks[socket] == zmq.POLLIN:
            answer = socket.recv() #ack
            logger.debug('recv: %s', answer)
            break
        logger.warn('(try %d) waited %d ms for "ack" from server',
                this_try, timeout)
        this_try += 1
        if this_try > max_tries:
            logger.error('could not send error message to server')
            logger.error('stopping 0MQ client anyway')


#----------------------------------------------------------


def close(logger, sockets, context):
    for socket in sockets:
        if socket is not None:
            socket.setsockopt(zmq.LINGER, 0)
            socket.close()

    context.term()
    logger.debug("0MQ client finished")


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


def main():

    """
    # This is an important outcome of this process and must be available
    # to different processing phases of this script
    """

    package = __name__.rsplit('.', 2)[0]
    version = package + ' v' + \
              __import__('pkg_resources').require(package)[0].version
    prog = os.path.basename(sys.argv[0])

    args = docopt.docopt(__doc__ % dict(prog=prog, version=version),
            version=version)


    # Setup the logging system
    formatter = logging.Formatter(fmt="[%(asctime)s - execute.py - " \
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


    # Retrieve the cache path
    cache = args['--cache'] if args['--cache'] is not None else '/cache'


    # Creates the 0MQ socket for communication with BEAT
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    address = args['<addr>']
    socket.connect(address)
    logger.debug("zmq client connected to `%s'", address)


    # Creates the 0MQ socket for communication with the databases (if necessary)
    db_socket = None
    if args['<db_addr>']:
        db_socket = context.socket(zmq.PAIR)
        db_socket.connect(args['<db_addr>'])
        logger.debug("zmq client connected to db `%s'", args['<db_addr>'])

    loop_socket = None
    if args['<loop_addr>']:
        loop_socket = context.socket(zmq.PAIR)
        loop_socket.connect(args['<loop_addr>'])
        logger.debug("zmq client connected to loop `%s'", args['<loop_addr>'])

    # Check the dir
    if not os.path.exists(args['<dir>']):
        send_error(logger, socket, 'sys', "Running directory `%s' not found" % args['<dir>'])
        close(logger, [socket, db_socket, loop_socket], context)
        return 1


    # Load the configuration
    with open(os.path.join(args['<dir>'], 'configuration.json'), 'r') as f:
        cfg = simplejson.load(f)


    # Create a new user with less privileges (if necessary)
    if os.getuid() != cfg['uid']:
        retcode = subprocess.call(['adduser', '--uid', str(cfg['uid']),
                                   '--no-create-home', '--disabled-password',
                                   '--disabled-login', '--gecos', '""', '-q',
                                   'beat-nobody'])
        if retcode != 0:
            send_error(logger, socket, 'sys', 'Failed to create an user with the UID %d' % cfg['uid'])
            close(logger, [socket, db_socket, loop_socket], context)
            return 1


        # Change to the user with less privileges
        try:
            os.setgid(cfg['uid'])
            os.setuid(cfg['uid'])
        except:
            import traceback
            send_error(logger, socket, 'sys', traceback.format_exc())
            close(logger, [socket, db_socket, loop_socket], context)
            return 1


    try:
        # Sets up the execution
        executor = AlgorithmExecutor(socket,
                            args['<dir>'],
                            cache_root=cache,
                            db_socket=db_socket,
                            loop_socket=loop_socket)

        try:
            status = executor.setup()
            if not status:
                raise UserError("Could not setup algorithm (returned False)")
        except (UserError, MemoryError):
            raise
        except Exception as e:
            import traceback
            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb = traceback.extract_tb(exc_traceback)
            s = process_traceback(tb, executor.prefix)
            raise UserError("%s%s: %s" % (s, type(e).__name__, e))

        # Prepare the algorithm
        try:
            status = executor.prepare()
            if not status:
                raise UserError("Could not prepare algorithm (returned False)")
        except (UserError, MemoryError):
            raise
        except Exception as e:
            import traceback
            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb = traceback.extract_tb(exc_traceback)
            s = process_traceback(tb, executor.prefix)
            raise UserError("%s%s: %s" % (s, type(e).__name__, e))

        # Execute the code
        try:
            status = executor.process()
            if not status:
                raise UserError("Could not run algorithm (returned False)")
        except (UserError, MemoryError):
            raise
        except Exception as e:
            import traceback
            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb = traceback.extract_tb(exc_traceback)
            s = process_traceback(tb, executor.prefix)
            raise UserError("%s%s: %s" % (s, type(e).__name__, e))

    except UserError as e:
        send_error(logger, socket, 'usr', str(e))
        return 1

    except MemoryError as e:
        # Say something meaningful to the user
        msg = "The user process for this block ran out of memory. We " \
            "suggest you optimise your code to reduce memory usage or, " \
            "if this is not an option, choose an appropriate processing " \
            "queue with enough memory."
        send_error(logger, socket, 'usr', msg)
        return 1

    except Exception as e:
        import traceback
        send_error(logger, socket, 'sys', traceback.format_exc())
        return 1

    finally:
        close(logger, [socket, db_socket, loop_socket], context)

    return 0


#----------------------------------------------------------


if __name__ == '__main__':
    sys.exit(main())

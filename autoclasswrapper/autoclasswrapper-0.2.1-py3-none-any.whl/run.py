"""autoclasswrapper: Python wrapper for AutoClass clustering.

Create run script and run classification
"""

import logging
import os
import subprocess


RUN_SCRIPT_CONTENT="""
# the "y" parameter validates warning
# in case of a reproducible run
autoclass -search {0}.db2 {0}.hd2 {0}.model {0}.s-params <<EOF
y
EOF
autoclass -reports {0}.results-bin {0}.search {0}.r-params

if [ $? -eq 0 ]
then
	touch autoclass-run-success
else
	touch autoclass-run-failure
fi
"""

log = logging.getLogger(__name__)


class Run():
    """Autoclass running script.

    Parameters
    ----------
    root_name : string (default "autoclass")
        Root name for input files and running script.
        Example: "autoclass" will lead to "autoclass.db2",
        "autoclass.model", "autoclass.sh"...
    tolerate_error : bool (default: False)
        If True, countinue generation of autoclass input files even if an
        error is encounter.
        If False, stop at first error.

    Attributes
    ----------
    had_error : bool (defaut False)
        Set to True if an error has been found in the generation of autoclass
        input files.

    """

    def __init__(self,
                 root_name="autoclass",
                 tolerate_error=False):
        """Instantiate object."""
        self.root_name = root_name
        self.tolerate_error = tolerate_error
        self.had_error = False

    def handle_error(f):
        """Handle error during data parsing and formating.

        Function decorator.

        Parameters
        ----------
        f : function

        Returns
        -------
        try_function : function wrapped into error handler

        """
        def try_function(self, *args, **kwargs):
            if self.tolerate_error or not self.had_error:
                try:
                    return f(self, *args, **kwargs)
                except Exception as e:
                    for line in str(e).split('\n'):
                        log.error(line)
                    self.had_error = True
        try_function.__name__ = f.__name__
        try_function.__doc__ = f.__doc__
        return try_function

    @handle_error
    def create_run_file(self):
        """Create bash script that runs AutoClass C."""
        log.info("Writing run file")
        run_name = self.root_name + ".sh"
        with open(run_name, "w") as runfile:
            # the "y" paramter is to validate warning
            # is case of for reproducible run
            runfile.write(RUN_SCRIPT_CONTENT.format(self.root_name))

    @handle_error
    def create_run_file_test(self, time=60):
        """Create dummy script.

        Scrit will wait for xx seconds
        while touching .log file every second.

        Parameters
        ----------
        time : int (default: 60)
            Time in seconds to wait.

        """
        log.info("Writing dummy run file")
        run_name = self.root_name + ".sh"
        log_name = self.root_name + ".log"
        rlog_name = self.root_name + ".rlog"
        with open(run_name, "w") as runfile:
            runfile.write("for a in $(seq 1 {}) \n".format(time))
            runfile.write("do \n")
            runfile.write("touch {} \n".format(log_name))
            runfile.write("sleep 1 \n")
            runfile.write("done \n")
            runfile.write("touch {} \n".format(rlog_name))

    @handle_error
    def run(self, tag=""):
        """Run autoclass clustering.

        autoclass-c executable must be in PATH!

        Parameters
        ----------
        tag : string (default: "")
            Tag to identify the autoclass run among other processes

        """
        log.info("Running clustering...")
        run_name = self.root_name + ".sh"
        proc = subprocess.Popen(['nohup', 'bash', run_name, tag],
                                env=os.environ)

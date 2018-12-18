
import re
import sys
import os
import subprocess
from . import genera
from ._version import __version__

__all__ = ['lifelib_dir', 'compile_rules', 'load_rules', 'reset_tree']

lifelib_dir = os.path.dirname(os.path.abspath(__file__))
this_python = os.path.abspath(sys.executable)
cygwin_dirs = []


def add_cygdir(*args):

    for a in args:
        cygwin_dirs.append(a)


def get_cygwin_dir():

    cygwin_possibilities = cygwin_dirs + [os.path.join(lifelib_dir, 'cygwin', 'cygwin64'), 'C:\\cygwin64']

    for c in cygwin_possibilities:
        if os.path.exists(c) and os.path.exists(os.path.join(c, 'bin')):
            return c

    raise ValueError("Cygwin directory unknown; please call lifelib.add_cygdir(r'D:\\path\\to\\cygwin64') or lifelib.install_cygwin()")


def install_cygwin(root_directory=None, packages=['python2', 'python2-numpy', 'python3', 'python3-numpy', 'gcc-g++', 'make', 'git']):
    '''
    For lifelib to run correctly on Windows, there needs to be a 64-bit Cygwin
    installation with g++, Python, and numpy. The user is free to download and
    configure Cygwin herself; this is provided as a speedy alternative which
    includes the prerequisites by default.

    This will eventually result in a directory tree resembling the following:

    lifelib--+--cygwin--+--cygwin-x86_64.exe
             |          |
             |          +--packages
             |          |
             |          +--cygwin64--+--bin-----bash.exe
             |                       |
             +--autocompile.py       +--etc
             |                       |
             +--cygbash.sh           +--usr
             |                       |
           [...]                   [...]

    This has a certain elegance that uninstalling lifelib will remove the
    internal Cygwin installation.
    '''

    try:
        from urllib import urlretrieve
    except ImportError:
        from urllib.request import urlretrieve

    package_directory = os.path.join(lifelib_dir, 'cygwin', 'packages')
    cygwin_setup = os.path.join(lifelib_dir, 'cygwin', 'cygwin-x86_64.exe')

    if root_directory is None:
        root_directory = os.path.join(lifelib_dir, 'cygwin', 'cygwin64')

    print("Preparing to install cygwin64 into %s..." % root_directory)

    if not os.path.exists(package_directory):
        os.makedirs(package_directory)

    # Remove the setup-x86_64 executable if it already exists.
    if os.path.exists(cygwin_setup):
        os.remove(cygwin_setup)

    # By downloading through HTTPS, the setup-x86_64 executable is secure
    # against man-in-the-middle attacks. Beyond that, individual packages
    # are secured by means of digital signatures and SHA-512 hashes; the
    # public-key used to verify those is embedded in setup-x86_64.
    print("Downloading Cygwin setup over HTTPS...")
    urlretrieve("https://cygwin.com/setup-x86_64.exe", cygwin_setup)

    args=[cygwin_setup, '-q', '--no-admin', '-n', '-N', '-d',
            '-R', root_directory, '-l', package_directory,
            '-s', 'http://mirrors.kernel.org/sourceware/cygwin',
            '-P', ','.join(packages)]

    # We are running in Linux, Mac OS X, or already inside Cygwin. In these
    # cases, it does not make sense to install Cygwin.
    if (os.name != 'nt'):
        print("Skipping Cygwin installation since os.name != 'nt'.")
        return

    # Install Cygwin into a subdirectory of lifelib, complete with all of
    # the dependencies used by lifelib.
    print("Installing Cygwin...")
    subprocess.check_call(args)
    verify_installation()

    print("Installation complete.")


def verify_installation():

    from .pythlib.lowlevel import regstring

    print("Verifying installation...")
    subprocess.check_call(get_local_bash() + ['echo', 'SUCCESS'])

    print("Verifying numpy is installed...")
    np_version = subprocess.check_output(get_local_bash() + ['python', '-c', 'import numpy as np; print(np.__version__)'])
    np_version = regstring(np_version).strip()
    print("Numpy version: %s" % np_version)
    return np_version


def get_local_bash():

    if (os.name == 'nt'):
        return [os.path.join(get_cygwin_dir(), 'bin', 'bash.exe'), os.path.join(lifelib_dir, 'cygbash.sh')]
    else:
        return ['bash', os.path.join(lifelib_dir, 'cygbash.sh')]


def get_local_python():

    if (os.name == 'nt'):
        return 'python'
    else:
        return this_python


def get_compiler():

    if (os.name == 'nt'):
        return get_local_bash() + ['g++']
    else:
        return ['g++']


def run_tests():

    print("Warning: if you are in a Jupyter notebook you will not see output until the tests complete.")
    print("Use the terminal to view periodic progress...")
    subprocess.check_call(get_local_bash() + ['tests/test_all.sh', this_python])
    print("Completed tests successfully.")


def compile_rules(*rules, **kwargs):

    if (len(rules) == 0):
        rules = ['b3s23']

    if (len(rules) > 8):
        raise ValueError("Each lifelib session may have up to 8 rules.")

    soname = os.path.join(lifelib_dir, 'pythlib', 'lifelib_%s.so' % '_'.join(rules))

    force_compile = kwargs.get('force_compile', False)
    verify_version = kwargs.get('verify_version', True)

    if force_compile or not os.path.exists(soname):
        recompile = True
    elif verify_version:
        from .pythlib import Session
        local_bash = get_local_bash()
        local_python = kwargs.get('local_python', get_local_python())
        sess = Session(soname, rules=rules, local_bash=local_bash, local_python=local_python)
        compiled_version = sess.lifelib.version
        python_version = __version__
        if compiled_version != python_version:
            sys.stderr.write('Compiled version %s does not match current version %s; recompiling...\n' % (compiled_version, python_version))
            recompile = True
        else:
            recompile = False
    else:
        recompile = False

    if recompile:

        try:

            cwd = os.path.abspath(os.getcwd())

            print("Generating code for rules %s..." % str(list(rules)))
            generate_code(rules)
            os.chdir(lifelib_dir)

            print("Compiling lifelib shared object (this may take a while)...")
            po = subprocess.Popen(get_compiler() + ["-std=c++11", "-march=native", "-O3",
                "-Wall", "-Wextra", "-fPIC", "-shared", "-o", soname, "lifelib.cpp"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            g_stdout, g_stderr = po.communicate()
            status = po.returncode

            if kwargs.get('compiler_output', (status != 0)):
                sys.stderr.write("Compiler stdout: %s\n" % g_stdout)
                sys.stderr.write("Compiler stderr: %s\n" % g_stderr)

            if (status != 0):
                raise RuntimeError("g++ returned nonzero exit code %d" % status)

        finally:

            os.chdir(cwd)

        reset_tree()
            
    return soname


def load_rules(*rules, **kwargs):

    rules = [r.lower() for r in rules]

    soname = compile_rules(*rules, **kwargs)
    from .pythlib import Session
    use_indirection = (os.name == 'nt') or kwargs.get('force_indirect', False)
    local_bash = get_local_bash() if use_indirection else None
    local_python = kwargs.get('local_python', get_local_python())

    # Choose the default number of planes to accommodate every rule
    # for which the lifetree has been compiled, including LifeHistory:
    default_planes = 1 + max([genera.rule_property(r, 'bitplanes') for r in rules])
    default_planes = max(4, default_planes)

    return Session(soname, rules=rules, local_bash=local_bash,
                    local_python=local_python, default_planes=default_planes)


def write_all_iterators(f, hist, rules, families):

    params = 'int n, uint64_t * inleaves'
    params2 = 'uint32_t* d'
    xparams = 'n, inleaves'
    xparams2 = 'd'

    if (hist):
        params += ', uint64_t * hleaves'
        xparams += ', hleaves'
        params2 += ', uint32_t* h'
        xparams2 += ', h'

    if (hist >= 2):
        params += ', uint64_t * jleaves'
        xparams += ', jleaves'
        params2 += ', uint32_t* j'
        xparams2 += ', j'

    params += ', uint64_t * outleaf'
    params2 += ', uint32_t * diffs'
    xparams += ', outleaf'
    xparams2 += ', diffs'

    f.write('    int iterate_var_leaf(int rule, %s) {\n' % params)
    f.write('        switch(rule) {\n')

    not_used = True
    nnot_used = True
    for (i, (runsafe, family)) in enumerate(zip(rules, families)):
        r = runsafe.replace('-', '_')

        if (family == 0):
            not_used = False
            nnot_used = False
            f.write('            case %d :\n' % i)
            f.write('                return %s::iterate_var_leaf(%s);\n' % (r, xparams))
        elif ((family == 2) and (hist == 1)):
            not_used = False
            f.write('            case %d :\n' % i)
            f.write('                return %s::iterate_var_leaf(inleaves, hleaves, outleaf);\n' % r)
        elif ((family != 2) and (hist == 0)):
            not_used = False
            f.write('            case %d :\n' % i)
            f.write('                return %s::iterate_var_leaf(inleaves, outleaf);\n' % r)
    f.write('        }\n')
    if not_used:
        f.write('        (void) %s;\n' % (xparams.replace(',', '; (void)')))
    elif nnot_used:
        f.write('        (void) n;\n')
    f.write('        return -1;\n')
    f.write('    }\n\n')

    def vlife_var(fname, lifeonly):

        f.write('    int %s(int rule, %s) {\n' % (fname, params2))
        f.write('        switch(rule) {\n')

        not_used = True
        for (i, (runsafe, family)) in enumerate(zip(rules, families)):
            r = runsafe.replace('-', '_')
            if ((r == 'b3s23') if lifeonly else (family == 0)):
                not_used = False
                f.write('            case %d :\n' % i)
                f.write('                return %s::%s(%s);\n' % (r, fname, xparams2))
        f.write('        }\n')
        if not_used:
            f.write('        (void) %s;\n' % (xparams2.replace(',', '; (void)')))
        f.write('        return -1;\n')
        f.write('    }\n\n')

    vlife_var('iterate_var_32_28', False)
    f.write('\n\n#ifdef __AVX512F__\n\n')
    vlife_var('iterate_var_48_28', True)
    f.write('\n\n#endif\n\n')


def reset_tree(rule='b3s23'):

    try:
        cwd = os.path.abspath(os.getcwd())
        generate_code([rule], clean_before=True)
    except:
        import warnings
        warnings.warn("Could not reset tree -- check permissions?")
    finally:
        os.chdir(cwd)


def generate_code(rules, clean_before=False):

    logic_directory = 'avxlife/lifelogic'

    # Determine rule families from genera:
    try:
        families = [genera.rule_property(r, 'family') for r in rules]
    except ImportError:
        print("ImportError; current directory == %s" % os.getcwd())
        raise

    os.chdir(lifelib_dir)

    if clean_before and os.path.exists(logic_directory):
        import shutil
        shutil.rmtree(logic_directory)

    if not os.path.exists(logic_directory):
        os.makedirs(logic_directory)
    os.chdir(logic_directory)

    # Obtain integers describing valid mantissae:
    def mant2int(m):
        if hasattr(m, '__iter__'):
            m = sum([(1 << x) for x in range(9) if x in m])
        return (m | 1)
    mantissae = [mant2int(genera.rule_property(r, 'mantissa')) for r in rules]

    # Write the main entry point:
    with open('iterators_all.h', 'w') as f:

        f.write('#pragma once\n')
        f.write('#include <string>\n')

        #include the generated code for each rule:
        for rulestring in rules:
            f.write('#include "iterators_%s.h"\n' % rulestring)

        f.write('namespace apg {\n\n')

        # Function to convert rulestring to rule integer:
        f.write('    int rule2int(std::string rule) {\n')
        for (i, r) in enumerate(rules):
            f.write('        if (rule == "%s") { return %d; }\n' % (r, i))
        f.write('        return -1;\n')
        f.write('    }\n\n')

        # Function to obtain family code from rule integer:
        f.write('    int uli_get_family(int rule) {\n')
        f.write('        switch (rule) {\n')
        for x in enumerate(families):
            f.write('            case %d : return %d;\n' % x)
        f.write('        }\n')
        f.write('        return 0;\n')
        f.write('    }\n\n')

        # Function to obtain mantissae from rule integer:
        f.write('    uint64_t uli_valid_mantissa(int rule) {\n')
        f.write('        switch (rule) {\n')
        for x in enumerate(mantissae):
            f.write('            case %d : return %d;\n' % x)
        f.write('        }\n')
        f.write('        return 3;\n')
        f.write('    }\n\n')

        for hist in range(3):
            write_all_iterators(f, hist, rules, families)

        f.write('}\n')

    # Create the source code for the rules:
    for r in rules:

        genera.create_rule(r)

    os.chdir(lifelib_dir)


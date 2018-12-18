
import os
import subprocess
from ctypes import *
from numbers import Integral

try:
    import cPickle as pickle
except ImportError:
    import pickle

import base64

__all__ = ['tzcount', 'call_underlying', 'WrappedLibrary', 'binstring', 'regstring']

def binstring(x):

    if x is None:
        return binstring('')
    elif type(x).__name__ == 'bytes':
        return x
    else:
        return x.encode('utf-8')

def make_compatible(x):

    if isinstance(x, tuple) and (len(x) == 1):
        return c_void_p(x[0])
    elif isinstance(x, list) and (len(x) == 1):
        return create_string_buffer(x[0])
    elif isinstance(x, list) and (len(x) >= 2):
        return ([c_uint64, c_int64, c_uint32, c_int32][x[0]] * x[1])()
    elif hasattr(x, 'ctypes'):
        import numpy as np
        return np.ascontiguousarray(x)
    elif hasattr(x, 'encode'):
        return x.encode('utf-8')
    else:
        return x

def regstring(x):

    if isinstance(x, str):
        return x
    else:
        return x.decode('utf-8')

def tzcount(x):

    return bin(x)[::-1].find('1')

def ensure_stack(required):

    if (required % 4096):
        required += (4096 - (required % 4096))

    try:
        import resource
        sl, hl = resource.getrlimit(resource.RLIMIT_STACK)
        if (sl < required):
            resource.setrlimit(resource.RLIMIT_STACK, (required, hl))
            sl, hl = resource.getrlimit(resource.RLIMIT_STACK)
            return (sl, hl)
    except Exception as e:
        return None


restypes = {'DeletePattern': None, 'GetBeszelIndex': c_uint64, 'GetUlqomaIndex': c_uint64, 'GetDiameterOfPattern': None,
            'AdvancePattern': c_void_p, 'GetSemisolidForPattern': c_void_p, 'BooleanPatternMutable': None,
            'BooleanPatternImmutable': c_void_p, 'TransformPattern': c_void_p, 'ShiftPattern': c_void_p,
            'FindPeriodOrAdvance': c_void_p, 'GetDTOfPattern': c_int64, 'GetDXOfPattern': c_int64,
            'GetDYOfPattern': c_int64, 'GetApgcodeOfPattern': None, 'SavePatternRLE': None, 'SavePatternMC': None,
            'GetPopulationOfPattern': None, 'CreateLifetree': c_void_p, 'CreatePatternFromRLE': c_void_p,
            'CreateRectangle': c_void_p, 'DeleteLifetree': None, 'GetPatternBox': None, 'PatternEquality': c_bool,
            'PatternNonempty': c_bool, 'MatchLive': c_void_p, 'MatchLiveAndDead': c_void_p, 'GetRuleOfPattern': None,
            'GetSolidForPattern': c_void_p, 'GetOriginState': c_uint64, 'GetCells': None, 'SetCells': None,
            'CreatePatternFromFile': c_void_p, 'MakeSpaceshipStream': c_void_p, 'GetCompiledVersion': None,
            'GetCoords': None, 'GetPatternBound': c_uint64, 'GetSubpops': None, 'Hashsoup': c_void_p}


def call_underlying(lifelib, fname_and_args):

    fname = regstring(fname_and_args[0])
    args = fname_and_args[1:]

    if (fname == 'EnsureStack'):
        return ensure_stack(args[0])

    retpos = -1
    retsize = 0

    returnables = [list]

    for (i, x) in enumerate(args):
        if isinstance(x, list):
            retpos = i
            retsize = len(x)
        elif hasattr(x, 'ctypes'):
            retpos = i
            retsize = 2

    args = [make_compatible(x) for x in args]

    try:
        func = getattr(lifelib, fname)
    except AttributeError:
        if 'Version' in fname:
            return "old"
        else:
            raise

    rt = restypes[fname]
    if rt is not None:
        func.restype = rt

    def f(i, a):
        if hasattr(a, 'ctypes'):
            return c_void_p(a.ctypes.data)
        elif (retpos != i):
            return a
        elif (retsize == 1):
            return cast(a, c_void_p)
        else:
            return a

    retval = func(*[f(i, a) for (i, a) in enumerate(args)])

    if (rt is not None) and (rt == c_void_p):
        if isinstance(retval, c_void_p):
            retval = tuple([retval.value])
        else:
            retval = tuple([retval])
    elif (retpos >= 0):
        if hasattr(args[retpos], 'ctypes'):
            retval = args[retpos]
        elif (retsize == 1):
            retval = regstring(args[retpos].value)
        else:
            retval = list(args[retpos])

    return retval


def remote_load():
    '''
    Minimalistic function which operates lifelib from instructions received
    from stdin. Results and exceptions are returned via stdout.
    '''

    from sys import argv, stdin, stdout, stderr
    from traceback import format_exc

    if hasattr(stdin, 'buffer'):
        stdin = stdin.buffer

    if hasattr(stdout, 'buffer'):
        stdout = stdout.buffer

    the_library = cdll.LoadLibrary(argv[1])

    while True:

        obj = pickle.load(stdin)

        if (len(obj[0]) <= 1):
            break

        try:
            retval = (0, call_underlying(the_library, obj))
        except Exception:
            retval = (1, format_exc())

        pickle.dump(retval, stdout, 2)
        stdout.flush()

    pickle.dump((0, 0), stdout, 2)
    stdout.flush()


class WrappedLibrary(object):

    def __init__(self, soname, local_bash=None, local_python='python'):

        soname = os.path.abspath(soname)

        if local_bash is None:
            self.the_library = cdll.LoadLibrary(soname)
            self.remote = False
        else:
            args = local_bash + [local_python, 'pythlib/lowlevel.py', soname]
            self.the_library = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            self.remote = True

    @property
    def version(self):

        v = self('GetCompiledVersion', [2048]).lower()
        while (len(v) >= 1) and (v[0] == 'l'):
            v = v[1:]

        return v

    def __call__(self, *args):

        if self.remote:
            pickle.dump(tuple(args), self.the_library.stdin, 2)
            self.the_library.stdin.flush()
            retval = pickle.load(self.the_library.stdout)

            if retval[0] == 0:
                return retval[1]
            else:
                raise RuntimeError("Child process raised exception: %s" % str(retval[1]))
        else:
            return call_underlying(self.the_library, args)

    def ensure_limit(self, exponent, mantissa, pname='Parameter'):

        powerof2 = exponent + len(bin(abs(mantissa) - 1)) - 2

        if (powerof2 > 65536):
            raise ValueError("%s exceeds maximum of 2 ^^ 5" % pname)

        if (powerof2 > 800):
            x = self('EnsureStack', powerof2 * 768)
            if x is None:
                import warnings
                warnings.warn("Could not ensure stack size, probably due to running on Windows. Expect segfaults soon.")
            else:
                print("Stack size limit increased to (%d, %d)" % x)

    def __del__(self):

        if self.remote:
            try:
                self.__call__('X', 0)
            except Exception:
                pass
            self.the_library.wait()
            self.the_library.stdin.close()
            self.the_library.stdout.close()

if __name__ == '__main__':

    remote_load()

# This file is generated by C:\projects\scipy-wheels\scipy\setup.py
# It contains system_info results at the time of building this package.
__all__ = ["get_info","show"]


import os
extra_dll_dir = os.path.join(os.path.dirname(__file__), 'extra-dll')
if os.path.isdir(extra_dll_dir):
    os.environ["PATH"] += os.pathsep + extra_dll_dir
blas_opt_info={'libraries': ['openblas'], 'language': 'f77', 'define_macros': [('HAVE_CBLAS', None)], 'library_dirs': ['C:\\projects\\scipy-wheels\\scipy\\build\\openblas']}
lapack_mkl_info={}
openblas_info={'libraries': ['openblas'], 'language': 'f77', 'define_macros': [('HAVE_CBLAS', None)], 'library_dirs': ['C:\\projects\\scipy-wheels\\scipy\\build\\openblas']}
openblas_lapack_info={'libraries': ['openblas'], 'language': 'f77', 'define_macros': [('HAVE_CBLAS', None)], 'library_dirs': ['C:\\projects\\scipy-wheels\\scipy\\build\\openblas']}
lapack_opt_info={'libraries': ['openblas'], 'language': 'f77', 'define_macros': [('HAVE_CBLAS', None)], 'library_dirs': ['C:\\projects\\scipy-wheels\\scipy\\build\\openblas']}
blas_mkl_info={}
blis_info={}

def get_info(name):
    g = globals()
    return g.get(name, g.get(name + "_info", {}))

def show():
    for name,info_dict in globals().items():
        if name[0] == "_" or type(info_dict) is not type({}): continue
        print(name + ":")
        if not info_dict:
            print("  NOT AVAILABLE")
        for k,v in info_dict.items():
            v = str(v)
            if k == "sources" and len(v) > 200:
                v = v[:60] + " ...\n... " + v[-60:]
            print("    %s = %s" % (k,v))
    
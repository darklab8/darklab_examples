from cffi import FFI

def build():
    ffibuilder = FFI()

    ffibuilder.cdef("float pi_approx(int n);")

    ffibuilder.set_source("_pi",  # name of the output C extension
    """
        #include "pi.h"
    """,
        sources=['pi.c'],   # includes pi.c as additional sources
        libraries=['m'])    # on Unix, link with the math library

    ffibuilder.compile(verbose=True, tmpdir="simple_python_with_c_extension")

if __name__ == "__main__":
    build()
    
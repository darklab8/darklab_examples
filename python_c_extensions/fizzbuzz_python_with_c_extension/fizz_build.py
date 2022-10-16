from cffi import FFI
from pathlib import Path

def build():
    ffibuilder = FFI()

    h_file_name = "fizz.h"
    with open(str(Path("fizzbuzz_python_with_c_extension") / h_file_name), "r") as file:
        h_file_content = file.read()
    ffibuilder.cdef(h_file_content)

    ffibuilder.set_source("_fizz",  # name of the output C extension
    f"""
        #include "{h_file_name}"
    """,
        sources=['fizz.c'],   # includes *.c as additional sources
        libraries=['m'])    # on Unix, link with the math library

    ffibuilder.compile(verbose=True, tmpdir="fizzbuzz_python_with_c_extension")

if __name__ == "__main__":
    build()
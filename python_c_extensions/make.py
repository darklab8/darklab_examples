import argparse
from enum import Enum, auto
import subprocess
import fizzbuzz_python_only
import fizzbuzz_python_with_c_extension
import simple_python_with_c_extension
from pathlib import Path

class Actions(Enum):
    simple_c = auto()
    simple_cpp = auto()
    simple_c_ext = auto()
    fizz_py_only = auto()
    fizz_py_ext = auto()

def main():
    parser = argparse.ArgumentParser()
    actions_parser = parser.add_subparsers(dest="action", required=True)

    actions_parser.add_parser(Actions.simple_c.name, help="Check that we can compile C")
    actions_parser.add_parser(Actions.simple_cpp.name, help="Check that we can compile C++")
    actions_parser.add_parser(Actions.simple_c_ext.name, help="Try build and running simple python with C extension")
    actions_parser.add_parser(Actions.fizz_py_only.name, help="Run fizzbuzz without C/C++ extensions")
    actions_parser.add_parser(Actions.fizz_py_ext.name, help="Run fizzbuzz with C/C++ extensions")

    args = parser.parse_args()

    def simple_c_or_cpp_build_run_cmd(compiler: str, folder: str, source: str, dest: str = "hello"):
        return (
            f"{compiler} -Wall {str(Path(folder) / source)}"
            f" -o {str(Path(folder) / dest)}"
            f" && ./{str(Path(folder) / dest)}"
        )


    match Actions[args.action]:
        case Actions.simple_c:
            subprocess.run(simple_c_or_cpp_build_run_cmd(compiler="gcc", folder="simple_c_program", source="hello.c"), shell=True, check=True)
        case Actions.simple_cpp:
            subprocess.run(simple_c_or_cpp_build_run_cmd(compiler="g++", folder="simple_cpp_program", source="hello.cpp"), shell=True, check=True)
        case Actions.simple_c_ext:
            simple_python_with_c_extension.build()
            simple_python_with_c_extension.run()
        case Actions.fizz_py_only:
            fizzbuzz_python_only.run()

        case Actions.fizz_py_ext:
            fizzbuzz_python_with_c_extension.build()
            fizzbuzz_python_with_c_extension.run()
        case _:
            raise NotImplementedError("Not implemented Action")

if __name__=="__main__":
    main()
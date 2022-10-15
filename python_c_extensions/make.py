import argparse
from enum import Enum, auto
import subprocess
from fizbuzz_pure import main as fizz_pure_main

class Actions(Enum):
    run_c = auto()
    run_cpp = auto()
    pi_extension = auto()
    fizz = auto()
    fizz_extension = auto()

def main():
    parser = argparse.ArgumentParser()
    actions_parser = parser.add_subparsers(dest="action", required=True)

    actions_parser.add_parser(Actions.run_c.name, help="Check that we can compile C")
    actions_parser.add_parser(Actions.run_cpp.name, help="Check that we can compile C++")
    actions_parser.add_parser(Actions.fizz.name, help="Run fizzbuzz without C/C++ extensions")
    actions_parser.add_parser(Actions.pi_extension.name, help="Run fizzbuzz without C/C++ extensions")
    actions_parser.add_parser(Actions.fizz_extension.name, help="Run fizzbuzz without C/C++ extensions")

    args = parser.parse_args()

    match Actions[args.action]:
        case Actions.run_c:
            subprocess.run("gcc -Wall hello.c -o hello && ./hello", shell=True, check=True)
        case Actions.run_cpp:
            subprocess.run("g++ -Wall hello.c -o hello && ./hello", shell=True, check=True)
        case Actions.fizz:
            fizz_pure_main()
        case Actions.pi_extension:
            subprocess.run("python3 pi_extension_build.py && python3 pi_app.py", shell=True, check=True)
        case Actions.fizz_extension:
            subprocess.run("python3 fizz_extension_build.py && python3 fizz_run.py", shell=True, check=True)
        case _:
            raise NotImplementedError("Not implemented Action")

if __name__=="__main__":
    main()
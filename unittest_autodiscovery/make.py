import subprocess
import sys

def main():
    
    match sys.argv[1:]:
        case ['tests']:
            subprocess.run("python3 -m unittest discover", shell=True, check=True)
        case _:
            raise NotImplementedError("not registered match-case")

if __name__=="__main__":
    main()
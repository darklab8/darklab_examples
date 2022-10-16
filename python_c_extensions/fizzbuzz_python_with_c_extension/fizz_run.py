import functools
from time import time
import sys
from pathlib import Path

def time_measure(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished at {time()-start}")
        return result

    return wrapper

@time_measure
def run():
    sys.path.append(str(Path(__file__).parent))
    try:
        from _fizz.lib import fizz
        from _fizz import ffi
    except ModuleNotFoundError as err:
        print(f"unable to load module, {err=}")

    result = fizz(1000000)

    print(f"{len(ffi.string(result))=}")
    print("success")
    

    del result

if __name__=="__main__":
    run()
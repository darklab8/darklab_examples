from contextlib import suppress
from pathlib import Path
import sys

def run():
    sys.path.append(str(Path(__file__).parent))
    try:
        from _pi.lib import pi_approx
    except ModuleNotFoundError as err:
        print(f"unable to load module, {err=}")

    approx = pi_approx(10)
    assert str(approx).startswith("3.")

    approx = pi_approx(10000)
    assert str(approx).startswith("3.1")

    print("success")
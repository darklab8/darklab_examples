from time import time
import functools

def time_measure(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished at {time()-start}")
        return result

    return wrapper

def fizzbuzz(n):
    return ("Fizz" * (not _ % 3) + "Buzz" *
            (not _ % 5) or f"{_ + 1}" for _ in range(n))

@time_measure
def fizz_result():
    return ", ".join(fizzbuzz(1000000))

@time_measure
def main():
    print(f"{len(fizz_result())=}")


if __name__ == "__main__":
    main()
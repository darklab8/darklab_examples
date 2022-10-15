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
    for number in range(1,n+1):
        if number % 3 == 0 and number % 5 == 0:
            yield b"FizzBuzz"
        elif number % 3 == 0:
            yield b"Fizz"
        elif number % 5 == 0:
            yield b"Buzz"
        else:
            # yield bin(number)
            yield str(number).encode()

@time_measure
def fizz_result():
    return b",".join(fizzbuzz(1000000))

@time_measure
def main():
    print(f"{len(fizz_result())=}")
    # print(fizz_result())


if __name__ == "__main__":
    main()
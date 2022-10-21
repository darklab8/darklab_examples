import functools

def revealer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func=}({args=}, {kwargs=})")
        result = func(*args, **kwargs)
        return result
    return wrapper
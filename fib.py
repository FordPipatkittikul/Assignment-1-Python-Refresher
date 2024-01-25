from functools import lru_cache
import time


def timer(func):
    def wrapper(*args):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        finish_time = end_time - start_time
        formatted_finish_time = f"{finish_time:.8f}"
        print(f"Finished in {formatted_finish_time}s: f({args[0]}) -> {result}")
        return result

    return wrapper


@lru_cache
@timer
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)




if __name__ == "__main__":
    fib(10)


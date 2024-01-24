import functools
import time
import matplotlib.pyplot as plt


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


@functools.lru_cache
@timer
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def make_a_grah(x_axis: range, y_axis: list):
    plt.plot(x_axis, y_axis)
    plt.xlabel("X axis: n (Fibonacci number index)")
    plt.ylabel("Y axis: Time (seconds)")
    plt.title("Fibonacci Function Timing")
    plt.ylim(bottom=0)
    plt.grid(True)

    # Show the graph
    plt.show()


if __name__ == "__main__":
    number = 100
    fib(number)
    # n_values = range(number + 1)  # Calculate Fibonacci numbers up to the 100th
    # execution_times = []

    # for n in n_values:
    #     _, elapsed_time = fib(n)  # Discard the actual Fibonacci number, store only time
    #     execution_times.append(elapsed_time)
    # make_a_grah(n_values,execution_times)

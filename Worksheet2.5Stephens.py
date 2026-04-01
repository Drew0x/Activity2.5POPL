#Decorator4

from functools import wraps
import time


def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds.")
        return result
    return wrapper


if __name__ == "__main__":
    @timing_decorator
    def example_function(n):
        total = 0
        for i in range(n):
            time.sleep(1)
            total += 1
        return total

    result = example_function(5)
    print(f"Result: {result}")


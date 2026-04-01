from functools import wraps
import datetime

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] {datetime.datetime.now() }: Executing {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] {datetime.datetime.now() }: Finished {func.__name__}")
        return result
    
    return wrapper
    
@log_decorator
def add_numbers(a, b):
    return a + b

total = add_numbers(10, 5)
print(f"The total is: {total}")
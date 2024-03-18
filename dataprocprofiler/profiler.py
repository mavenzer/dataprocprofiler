import time
import pandas as pd
import numpy as np
from functools import wraps

def profile_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Example wrapper for Pandas functions
def pandas_profiler(func):
    @profile_function
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# Example usage with a Pandas function
@pandas_profiler
def read_csv(file_path):
    return pd.read_csv(file_path)


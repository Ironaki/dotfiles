import functools
import json
from time import perf_counter


def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Entering function: {func.__name__}")
        start_time = perf_counter()
        res = func(*args, **kwargs)
        time_ms = round((perf_counter() - start_time) * 1000)
        print(f"Finished in {time_ms} ms")
        return res

    return wrapper


def print_json(json_data):
    print(json.dumps(json_data, indent=2, default=str))

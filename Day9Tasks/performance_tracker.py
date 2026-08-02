import time


def track_performance(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        execution_time = end_time - start_time
        print(f"'{func.__name__}' executed in {execution_time:.4f} seconds")

        return result
    return wrapper


@track_performance
def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


@track_performance
def slow_function():
    time.sleep(1)
    print("Slow function finished.")


result = calculate_sum(1000000)
print(f"Sum: {result}\n")

slow_function()

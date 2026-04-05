import time

def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()

    print(f"Time taken: {(end - start)*1000:.4f} ms")
    return result

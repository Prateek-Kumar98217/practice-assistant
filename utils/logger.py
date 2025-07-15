from datetime import time
def timed_node(name):
    def decorator(func):
        def wrapper(state):
            start=time.time()
            result=func(state)
            end=time.time()
            duration=end-start
            print(f"[{name}] took {duration:.3f} seconds")
            return result
        return wrapper
    return decorator
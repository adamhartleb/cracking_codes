from time import perf_counter


def timer(fn):
    def inner(*args):
        start = perf_counter()
        fn(*args)
        elapsed = perf_counter() - start
        print(f'{fn.__name__} took {elapsed:.2f} seconds to execute.')
    return inner

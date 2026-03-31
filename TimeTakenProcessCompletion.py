from time import time


def parent_func(func):
    def wrap_func():
        starting_time = time()
        result = func()
        ending_time = time()
        print(f'Function executed in {(ending_time - starting_time):.2}s')
        return result

    return wrap_func


@parent_func
def inner_func():
    for i in range(50):
        for j in range(1000):
            if (i * j) % 2 == 0:
                i * j

start_deco_time = time()
inner_func()
print(f'excute decorator time: {(time() - start_deco_time):.2}s')

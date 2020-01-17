# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
import random

N = 10

def gen(N):
    while (N):
        yield random.randrange(1, 100, 1)
        N -= 1

# написать генераторное выражение, которое делает то же самое
generator = (random.randrange(1, 100, 1) for i in range(N))

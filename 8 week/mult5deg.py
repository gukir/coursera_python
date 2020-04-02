import functools
from sys import stdin
print(
    functools.reduce(
        lambda x, y: x * y,
        map(
            lambda x: int(x)**5,
            stdin.readline().split())
    )
)

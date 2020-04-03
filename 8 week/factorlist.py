from sys import stdin
import itertools
print(
    1,
    *itertools.accumulate(
        range(
            1, int(stdin.readline()) + 1
        ),
        lambda x, y: x * y
    )
)

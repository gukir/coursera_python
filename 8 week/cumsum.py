from sys import stdin
import itertools
print(
    *itertools.accumulate(
        map(
            int,
            stdin.readline().split()
        )
    )
)

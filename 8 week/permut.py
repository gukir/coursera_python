from sys import stdin
import itertools
print(
    *sorted(
        map(
            lambda x: ''.join(x),
            itertools.permutations(
                map(
                    str,
                    range(1, int(stdin.readline()) + 1
                          )
                )
            )
        )
    ),
    sep='\n'
)

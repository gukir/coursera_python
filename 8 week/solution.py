from sys import stdin
import itertools
import operator
import functools
print(*functools.reduce(
        lambda v_test, b_test:
        next(
            filter(
                lambda variant:
                all(
                    map(
                        lambda bet:
                        operator.xor(variant.index(bet[0]) < variant.index(bet[1]),
                                     variant.index(bet[2]) < variant.index(bet[3])),
                        b_test
                    )
                ),
                v_test
            ), [0]
        ), functools.reduce(lambda k, n: [itertools.permutations(
            map(
                str, range(1, k + 1)
            )
        ), list(map(
            lambda tmp:
            stdin.readline().split(),
            range(n)
        ))
        ], map(int, stdin.readline().split()))
    ))

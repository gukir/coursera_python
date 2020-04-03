from sys import stdin
import functools
print(
    *functools.reduce(
        lambda list_x, list_y: map(
            lambda x, y: int(not int(x) and int(y) or
                             int(x) and not int(y)),
            list(list_x),
            list(list_y)
        ),
        map(
            lambda x: ''.join(stdin.readline().split()),
            range(int(stdin.readline()))
        )
    )
)

from sys import stdin
print(
    *map(
        lambda x, y: int(
            not int(x) and int(y) or
            int(x) and not int(y)
        ),
        stdin.readline().split(),
        stdin.readline().split()
    )
)

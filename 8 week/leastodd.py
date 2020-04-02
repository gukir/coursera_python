from sys import stdin
print(
    min(
        filter(
            lambda x: x % 2 != 0,
            map(
                int, stdin.readline().split()
            )
        )
    )
)

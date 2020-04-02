from sys import stdin
print(
    any(
        map(
            lambda x: int(stdin.readline()) == 0, range(int(stdin.readline()))
        )
            )
)

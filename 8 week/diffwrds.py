from sys import stdin
print(
    len(
        set(
            ''.join(stdin.readlines()).split()
        )
    )
)

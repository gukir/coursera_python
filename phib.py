def phib(n):
    if n < 3:
        return 1
    else:
        return phib(n - 1) + phib(n - 2)


i = int(input())
print(phib(i))

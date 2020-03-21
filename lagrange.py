def lagrange(n, k):
    if n == 0:
        return True
    elif k == 0:
        return False
    for i in range(1, 100):
        if n < i**2:
            return False
        if lagrange(n - i**2, k - 1):
            print(i, end=' ')
            return True


nn = int(input())
lagrange(nn, 4)

def cubesum(n, k):
    if k == 0:
        return False
    for i in range(round(n**(1/3))+1, 0, -1):
        i3 = i**3
        if i3 > n:
            continue
        if n == i3 or cubesum(n - i3, k - 1):
            print(i3, end=' ')
            return True
    return False


nn = int(input())
if not cubesum(nn, 7):
    print(0)

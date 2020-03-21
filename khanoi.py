def move(n, x, y):
    if n == 1:
        print(n, x, y)
    else:
        buf = 6 - x - y
        move(n - 1, x, buf)
        print(n, x, y)
        move(n - 1, buf, y)


n_i = int(input())
move(n_i, 1, 3)

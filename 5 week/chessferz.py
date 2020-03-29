field = list(range(1, 65))
bl = set()
beat_flag = False
for i in range(8):
    [x, y] = list(map(int, input().split()))
    pos = (y - 1) * 8 + x
    if pos in bl:
        beat_flag = True
    bl.update(range((y - 1) * 8 + 1, (y - 1) * 8 + 9))
    bl.update(range(x, 65, 8))
    for col in range(1 - x, 9 - x):
        for row in range(1 - y, 9 - y):
            if col != 0 and row != 0:
                if row // col == col // row:
                    bl.update([pos + row * 8 + col])
if beat_flag:
    print('YES')
else:
    print('NO')

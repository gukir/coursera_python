def distance(x1f, y1f, x2f, y2f):
    return ((x2f - x1f) ** 2 + (y2f - y1f) ** 2) ** (1 / 2)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(distance(x1, y1, x2, y2))

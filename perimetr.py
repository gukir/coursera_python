def distance(x1f, y1f, x2f, y2f):
    return ((x2f - x1f) ** 2 + (y2f - y1f) ** 2) ** (1 / 2)


def perimetr(x1f, y1f, x2f, y2f, x3f, y3f):
    return distance(x1f, y1f, x2f, y2f) + \
           distance(x1f, y1f, x3f, y3f) + \
           distance(x2f, y2f, x3f, y3f)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

print(perimetr(x1, y1, x2, y2, x3, y3))

def isdotunderline(x1f, y1f, a, b):
    if y1f <= a*x1f + b:
        return True
    return False


def isdotoverline(x1f, y1f, a, b):
    if y1f >= a*x1f + b:
        return True
    return False


def distance(x1f, y1f, x2f, y2f):
    return ((x2f - x1f) ** 2 + (y2f - y1f) ** 2) ** (1 / 2)


def isdotincircle(x1f, y1f, x0, y0, r):
    if distance(x1f, y1f, x0, y0) <= r:
        return True
    return False


def isdotoutcircle(x1f, y1f, x0, y0, r):
    if distance(x1f, y1f, x0, y0) >= r:
        return True
    return False


def IsPointInArea(x1f, y1f):
    return (isdotunderline(x1f, y1f, 2, 2) and
            isdotunderline(x1f, y1f, -1, 0) and
            isdotoutcircle(x1f, y1f, -1, 1, 2)) or \
           (isdotoverline(x1f, y1f, 2, 2) and
            isdotoverline(x1f, y1f, -1, 0) and
            isdotincircle(x1f, y1f, -1, 1, 2))


x1 = float(input())
y1 = float(input())

if IsPointInArea(x1, y1):
    print('YES')
else:
    print('NO')

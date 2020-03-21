def isdotinsquare(x1f, y1f):
    if not (not (y1f <= x1f + 1) or
            not (-x1f + 1 >= y1f) or
            not (y1f >= x1f - 1)) and\
            y1f >= -x1f - 1:
        return 'YES'
    return 'NO'


x1 = float(input())
y1 = float(input())
print(isdotinsquare(x1, y1))

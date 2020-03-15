a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a * b * c * d != 0.:
    if a * d - b * c != 0.:
        y = (f * a - e * c) / (a * d - b * c)
        x = (e - b * y) / a
        print(2, x, y)
    else:
        if e == 0. and f == 0.:
            print(1, -a / b, e / b)
        elif e == 0. or f == 0.:
            print(0)
        elif a * f - e * c == 0.:
            print(1, -a / b, e / b)
        else:
            print(0)
else:
    if b * c * d != 0.:
        y = e / b
        x = (f - d * y) / c
        print(2, x, y)
    elif a * c * d != 0.:
        x = e / a
        y = (f - c * x) / d
        print(2, x, y)
    elif a * b * d != 0.:
        y = f / d
        x = (e - b * y) / a
        print(2, x, y)
    elif a * b * c != 0.:
        x = f / c
        y = (e - a * x) / b
        print(2, x, y)
    else:
        if a * d != 0.:
            x = e / a
            y = f / d
            print(2, x, y)
        elif b * c != 0.:
            y = e / b
            x = f / c
            print(2, x, y)
        elif a * b != 0.:
            if f == 0.:
                print(1, -a/b, e/b)
            else:
                print(0)
        elif c * d != 0.:
            if e == 0.:
                print(1, -c/d, f/d)
            else:
                print(0)
        elif a * c != 0.:
            if e/a == f/c:
                print(3, e/a)
            else:
                print(0)
        elif b * d != 0.:
            if e/b == f/d:
                print(4, e/b)
            else:
                print(0)
        else:
            if a != 0.:
                if f == 0.:
                    print(3, e/a)
                else:
                    print(0)
            elif b != 0.:
                if f == 0.:
                    print(4, e/b)
                else:
                    print(0)
            elif c != 0.:
                if e == 0.:
                    print(3, f/c)
                else:
                    print(0)
            elif d != 0.:
                if e == 0.:
                    print(4, f/d)
                else:
                    print(0)
            else:
                if e == 0. and f == 0.:
                    print(5)
                else:
                    print(0)

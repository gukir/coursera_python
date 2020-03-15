a = float(input())
b = float(input())
c = float(input())
if a == 0.:
    if b == 0.:
        if c == 0.:
            print(3)
        else:
            print(0)
    else:
        print(1, -c/b)
else:
    D = b**2 - 4*a*c
    if D < 0.:
        print(0)
    elif D > 0.:
        roots = [0.5*(-b + D**0.5)/a, 0.5*(-b - D**0.5)/a]
        roots.sort()
        print(2, *roots)
    else:
        root = -0.5*b/a
        print(1, root)

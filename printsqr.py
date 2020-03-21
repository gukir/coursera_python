def printsqr():
    in_i = int(input())
    if in_i != 0:
        outval = printsqr()
        if in_i**(1/2) == round(in_i**(1/2)):
            print(in_i, end=' ')
            return True
        return outval


if not printsqr():
    print(0)

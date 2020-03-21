def gcd(af, bf):
    if not bf % af:
        return af
    else:
        return gcd(bf % af, af)


a = int(input())
b = int(input())
if a > b:
    a, b = b, a
print(gcd(a, b))

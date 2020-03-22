a, b, c, d, e = \
    int(input()),\
    int(input()),\
    int(input()),\
    int(input()),\
    int(input())
ans = 0
for x in range(1001):
    if a * x**3 + b * x**2 + c * x + d == 0:
        if x != e:
            ans += 1
print(ans)

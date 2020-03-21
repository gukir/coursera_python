def powz(a, n):
    ans = 1
    for i in range(abs(n)):
        if n < 0:
            ans /= a
        else:
            ans *= a
    return ans

a = float(input())
n = int(input())
print(powz(a, n))

def C(nf, kf):
    if kf == 0:
        return 1
    elif kf == 1:
        return nf
    elif kf == nf:
        return 1
    else:
        return C(nf - 1, kf - 1) + C(nf - 1, kf)


n = int(input())
k = int(input())
print(C(n, k))

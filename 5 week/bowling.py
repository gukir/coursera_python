[N, K] = list(map(int, input().split()))
kegls = N*['I']
for i in range(K):
    [frst, lst] = list(map(int, input().split()))
    kegls[frst - 1:lst] = (lst - frst + 1) * ['.']
print(''.join(kegls))

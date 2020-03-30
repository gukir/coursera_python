N = int(input())
keys = list(map(int, input().split()))
keys_status = []
n_push = int(input())
pushes = list(map(int, input().split()))
for ipush in pushes:
    keys[ipush - 1] -= 1
for ikey in keys:
    if ikey >= 0:
        keys_status.append('NO')
    else:
        keys_status.append('YES')
print(*keys_status, sep='\n')

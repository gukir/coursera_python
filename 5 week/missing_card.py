N = int(input())
miss_num = N
for i in range(1, N):
    miss_num += i
    miss_num -= int(input())
print(miss_num)

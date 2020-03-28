listA = list(map(int, input().split()))
grt = [float('-inf'), 0]
for i_num, num in enumerate(listA):
    if num > grt[0]:
        grt[0] = num
        grt[1] = i_num
print(*grt)

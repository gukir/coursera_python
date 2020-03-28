listA = list(map(int, input().split()))
gnum = 0
for i_num in range(1, listA.__len__() - 1):
    if listA[i_num] > listA[i_num - 1] and \
       listA[i_num] > listA[i_num + 1]:
        gnum += 1
print(gnum)

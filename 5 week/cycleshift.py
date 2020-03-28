listA = list(map(int, input().split()))
listA.append('tmp')
for i_num in range(listA.__len__() - 1, 0, -1):
    listA[i_num] = listA[i_num - 1]
listA[0] = listA[-1]
listA.pop()
print(*listA)

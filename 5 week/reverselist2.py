listA = list(map(int, input().split()))
Alen = listA.__len__()
for i_num in range(Alen // 2):
    listA[i_num], listA[Alen - i_num - 1] = \
        listA[Alen - i_num - 1], listA[i_num]
print(*listA)

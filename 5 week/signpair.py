listA = list(map(int, input().split()))
for i_num in range(1, listA.__len__()):
    if listA[i_num] * listA[i_num - 1] >= 0:
        print(listA[i_num - 1], listA[i_num])
        break

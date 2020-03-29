listA = list(map(int, input().split()))
res = []
for elem in listA:
    if listA.count(elem) == 1:
        res.append(elem)
print(*res)

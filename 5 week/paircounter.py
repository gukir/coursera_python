listA = list(map(int, input().split()))
setA = set(listA)
pairs = 0
for elem in setA:
    n = listA.count(elem)
    pairs += n * (n - 1) // 2
print(pairs)

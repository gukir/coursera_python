listA = list(map(int, input().split()))
pos_elem = int(input())
listA = listA[:pos_elem:] + listA[pos_elem+1::]
print(*listA)

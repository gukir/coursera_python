listA = list(map(int, input().split()))
listA.append('tmp')
pos_elem = list(map(int, input().split()))
listA[pos_elem[0] + 1::] = listA[pos_elem[0]:-1:]
listA[pos_elem[0]] = pos_elem[1]
print(*listA)

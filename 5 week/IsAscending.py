def IsAscending(A):
    max_elem = A[0]
    i = 1
    while i < A.__len__() and max_elem < A[i]:
        max_elem = A[i]
        i += 1
    return i == A.__len__()


listA = list(map(int, input().split()))
if IsAscending(listA):
    print('YES')
else:
    print('NO')

N = int(input())
citco = {}
for i_n in range(N):
    cocil = input().split()
    for i_c in range(1, len(cocil)):
        citco[cocil[i_c]] = cocil[0]
M = int(input())
for i in range(M):
    print(citco[input()])

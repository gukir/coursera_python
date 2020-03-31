N = int(input())
masslang = set()
alllangs = set()
for i_n in range(N):
    M = int(input())
    puplangs = set()
    for i_m in range(M):
        puplangs.add(input())
    alllangs.update(puplangs)
    if not i_n:
        masslang.update(puplangs)
    else:
        masslang.intersection_update(puplangs)
print(masslang.__len__())
print(*masslang, sep='\n')
print(alllangs.__len__())
print(*alllangs, sep='\n')

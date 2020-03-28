listA = list(map(int, input().split()))
maxpos = [0, 0]
minneg = [0, 0]
maxprod = -1
for i_e, elem in enumerate(listA):
    if elem > maxpos[1]:
        maxpos[0] = i_e
        maxpos[1] = elem
    elif elem < minneg[1]:
        minneg[0] = i_e
        minneg[1] = elem

for i_e, elem in enumerate(listA):
    if i_e == maxpos[0] or i_e == minneg[0]:
        continue
    if elem > 0:
        if elem * maxpos[1] > maxprod:
            maxprod = elem * maxpos[1]
            res = [elem, maxpos[1]]
    else:
        if elem * minneg[1] > maxprod:
            maxprod = elem * minneg[1]
            res = [minneg[1], elem]
print(*res)

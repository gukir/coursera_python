listA = list(map(int, input().split()))
if len(listA) < 4:
    reselems = listA[::]
else:
    maxelems = []
    minelems = []
    reselems = []
    maxelems.append(listA.pop(listA.index(max(listA))))
    if maxelems[0] == 0:
        reselems.extend(listA[:2:])
        reselems.append(maxelems[0])
    elif maxelems[0] < 0:
        reselems.append(maxelems[0])
        for i in range(2):
            reselems.append(listA.pop(listA.index(max(listA))))
    else:
        reselems.append(maxelems[0])
        maxelems.append(listA.pop(listA.index(max(listA))))
        if maxelems[1] <= 0:
            for i in range(2):
                reselems.append(listA.pop(listA.index(min(listA))))
        else:
            reselems.append(maxelems[1])
            reselems.append(listA.pop(listA.index(max(listA))))
            if len(listA) > 1:
                for i in range(2):
                    minelems.append(listA.pop(listA.index(min(listA))))
                if minelems[0] * minelems[1] > reselems[1] * reselems[2]:
                    reselems[1::] = minelems[::]
print(*reselems)

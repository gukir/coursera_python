listA = list(map(int, input().split()))
Petya = int(input())
Ppos = 1
for man in listA:
    if Petya <= man:
        Ppos += 1
print(Ppos)

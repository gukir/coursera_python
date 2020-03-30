size = int(input())
listA = list(map(int, input().split()))
listA.sort()
shoes_num = 0
for shoe in listA:
    if shoes_num == 0:
        if shoe >= size:
            size = shoe
            shoes_num += 1
    else:
        if shoe - size >= 3:
            size = shoe
            shoes_num += 1
print(shoes_num)

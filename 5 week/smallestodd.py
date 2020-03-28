listA = list(map(int, input().split()))
sml = float('inf')
for num in listA:
    if num < sml and num % 2 == 1:
        sml = num
print(sml)

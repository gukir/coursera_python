N = int(input())
poss = set(range(1, N + 1))
setY = []
setN = []
while True:
    nums = input()
    if 'HELP' in nums:
        break
    else:
        nums = set(map(int, nums.split()))
    ans = input()
    if ans == 'YES':
        poss.intersection_update(nums)
    elif ans == 'NO':
        poss.difference_update(nums)
print(*sorted(list(poss)))

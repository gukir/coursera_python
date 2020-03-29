in_list = list(map(int, input().split()))
in_set = set(in_list)
cntr = 0
for num in in_set:
    innum = in_list.count(num)
    if innum > cntr:
        cntr = innum
        freq_num = num
print(freq_num)

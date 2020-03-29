in_list = list(map(int, input().split()))
i = 0
zer_cntr = 0
while i < len(in_list):
    if in_list[i] == 0:
        in_list.pop(i)
        zer_cntr += 1
    else:
        i += 1
in_list.extend(zer_cntr*[0])
print(*in_list)

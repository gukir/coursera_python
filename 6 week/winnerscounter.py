fin = open('input.txt', 'r', encoding='utf8')
win_num = [1, 1, 1]
gr_mark = [-1, -1, -1]
for pupil in fin:
    pupil = list(pupil.strip().split())
    pupil[-1] = int(pupil[-1])
    pupil[-2] = int(pupil[-2])
    if gr_mark[pupil[-2] - 9] < pupil[-1]:
        gr_mark[pupil[-2] - 9] = pupil[-1]
        win_num[pupil[-2] - 9] = 1
    elif gr_mark[pupil[-2] - 9] == pupil[-1]:
        win_num[pupil[-2] - 9] += 1
print(*win_num)

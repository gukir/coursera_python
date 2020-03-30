fin = open('input.txt', 'r', encoding='utf8')
gr_mark = [0, 0, 0]
for pupil in fin:
    pupil = list(pupil.strip().split())
    pupil[-1] = int(pupil[-1])
    pupil[-2] = int(pupil[-2])
    if gr_mark[pupil[-2] - 9] < pupil[-1]:
        gr_mark[pupil[-2] - 9] = pupil[-1]
print(*gr_mark)

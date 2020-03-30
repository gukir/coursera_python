fin = open('input.txt', 'r', encoding='utf8')
classes = [9, 10, 11]
marks = [0, 0, 0]
counter = [0, 0, 0]
for pupil in fin:
    pupil = list(pupil.strip().split())
    pupil[-1] = int(pupil[-1])
    pupil[-2] = int(pupil[-2])
    for i_cl in range(3):
        if classes[i_cl] == pupil[2]:
            counter[i_cl] += 1
            marks[i_cl] += pupil[3]
for i_cl in range(3):
    marks[i_cl] /= counter[i_cl]
print(*marks)

fin = open('input.txt', 'r', encoding='utf8')
K = int(fin.readline())
puplist = []
for pupil in fin:
    pupil = list(pupil.strip().split())
    pupil[-3::] = list(map(int, pupil[-3::]))
    if pupil[-1] < 40 or pupil[-2] < 40 or pupil[-3] < 40:
        continue
    else:
        puplist.append([pupil[0:-3:], sum(pupil[-3::])])
puplist.sort(key=lambda pup: -pup[-1])
if puplist.__len__() <= K:
    print(0)
elif puplist[K][-1] == puplist[0][-1]:
    print(1)
else:
    while puplist[K][-1] == puplist[K - 1][-1]:
        K -= 1
    print(puplist[K-1][-1])

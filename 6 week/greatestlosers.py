fin = open('input.txt', 'r', encoding='utf8')
ppls = []
for pupil in fin:
    pupil = list(pupil.strip().split())
    pupil[-2::] = list(map(int, pupil[-2::]))
    ppls.append(pupil)
ppls.sort(key=lambda ppl: (ppl[-2], -ppl[-1]))
est = []
cl = ppls[0][-2] - 1
for ppl in ppls:
    if ppl[-2] > cl:
        grt_est = ppl[-1]
        cl = ppl[-2]
    elif ppl[-1] < grt_est:
        est.append(ppl[-1])
        grt_est = -1
print(*est)

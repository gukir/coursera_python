fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
candidates = dict()
votes = 0
for i_line in fin:
    i_line = i_line.strip()
    votes += 1
    candidates[i_line] = candidates.get(i_line, 0) + 1
i_c = 0
for cnd in sorted(candidates, key=lambda cndl: (-candidates[cndl], cndl)):
    if candidates[cnd] * 100 > votes * 50:
        print(cnd, file=fout)
        break
    elif i_c == 0:
        print(cnd, file=fout)
        i_c += 1
    else:
        print(cnd, file=fout)
        break

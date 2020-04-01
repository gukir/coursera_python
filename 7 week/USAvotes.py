fin = open('input.txt', 'r', encoding='utf8')
vts = dict()
for i_line in fin:
    state = i_line.split()
    vts[state[0]] = vts.get(state[0], 0) + int(state[1])
for candidate in sorted(vts):
    print(candidate, vts[candidate])

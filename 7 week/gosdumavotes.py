fin = open('input.txt', 'r', encoding='utf8')
duma = 450
parties = []
seats = dict()
votes = 0
for i_line in fin:
    lline = i_line.split()
    prt = ' '.join(lline[:-1:])
    vts = int(lline[-1])
    parties.append(prt)
    seats[prt] = seats.get(prt, list())
    seats[prt].append(vts)
    votes += vts
quot = votes / duma
seats_sum = 0
for st in seats:
    seats[st].append(int(seats[st][0] // quot))
    seats[st].append(seats[st][0] / quot - seats[st][1])
    seats_sum += seats[st][1]
parties_priority = []
for st in sorted(seats, key=lambda x: (-seats[x][2], -seats[x][0])):
    parties_priority.append(st)
i_pp = 0
while seats_sum < duma:
    seats[parties_priority[i_pp % len(parties_priority)]][1] += 1
    i_pp += 1
    seats_sum += 1
for prt in parties:
    print(prt, seats[prt][1])

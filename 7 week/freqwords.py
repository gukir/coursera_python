fin = open('input.txt', 'r', encoding='utf8')
wrds_d = dict()
for i_line in fin:
    words = i_line.split()
    for wrd in words:
        wrds_d[wrd] = wrds_d.get(wrd, 0) + 1
new_wrds = dict()
for wrd in sorted(wrds_d, reverse=True):
    new_wrds[wrds_d[wrd]] = wrd
for wrd in sorted(new_wrds, reverse=True):
    print(new_wrds[wrd])
    break

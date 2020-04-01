fin = open('input.txt', 'r', encoding='utf8')
wrds_d = dict()
for i_line in fin:
    words = i_line.split()
    for wrd in words:
        wrds_d[wrd] = wrds_d.get(wrd, 0) + 1
for wrd in sorted(wrds_d, key=lambda wrd: (-wrds_d[wrd], wrd)):
    print(wrd)

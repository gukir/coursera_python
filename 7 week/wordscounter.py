fin = open('input.txt', 'r', encoding='utf8')
i_counter = dict()
for i_line in fin:
    i_words = i_line.split()
    for wrd in i_words:
        print(i_counter.get(wrd, 0), end=' ')
        i_counter[wrd] = i_counter.get(wrd, 0) + 1

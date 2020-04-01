N = int(input())
worddict = dict()
for i_n in range(N):
    i_word = input()
    l_word = i_word.lower()
    worddict[l_word] = worddict.get(l_word, [])
    worddict[l_word].append(i_word)
mistakes = 0
i_text = input().split()
for word in i_text:
    l_word = word.lower()
    if l_word == word:
        mistakes += 1
    elif l_word in worddict:
        if word not in worddict[l_word]:
            mistakes += 1
    else:
        n_up = 0
        for letter in list(word):
            if letter.isupper():
                n_up += 1
        if n_up > 1:
            mistakes += 1
print(mistakes)

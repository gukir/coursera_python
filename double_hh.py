str_i = input()
lst_str = str_i.split('h')
print('h'.join((lst_str[0], 2 * ('h'.join(lst_str[1:-1])), lst_str[-1])))

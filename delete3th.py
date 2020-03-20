str_i = input()
lst_str = list(str_i)
del lst_str[0::3]
print(''.join(lst_str))

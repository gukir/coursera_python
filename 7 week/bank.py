fin = open('input.txt', 'r', encoding='utf8')
customers = dict()
for i_line in fin:
    comand, *input_com = i_line.split()
    if comand == 'DEPOSIT':
        customers[input_com[0]] = customers.get(input_com[0], 0) + \
            int(input_com[-1])
    elif comand == 'WITHDRAW':
        customers[input_com[0]] = customers.get(input_com[0], 0) - \
            int(input_com[-1])
    elif comand == 'BALANCE':
        print(customers.get(input_com[0], 'ERROR'))
    elif comand == 'TRANSFER':
        customers[input_com[0]] = customers.get(input_com[0], 0) - \
            int(input_com[-1])
        customers[input_com[1]] = customers.get(input_com[1], 0) + \
            int(input_com[-1])
    elif comand == 'INCOME':
        for cstm in customers:
            if customers[cstm] > 0:
                customers[cstm] += customers[cstm] * \
                                   int(input_com[-1]) // 100

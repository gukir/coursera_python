def makeunuc(number):
    number = number.replace('(', '-')
    number = number.replace(')', '-')
    number = ''.join(number.split('-'))
    if len(number) == 7:
        number = '+7495' + number
    elif number.startswith('8'):
        number = '+7' + number[1::]
    return number


newnum = makeunuc(input())
for i in range(3):
    if newnum == makeunuc(input()):
        print('YES')
    else:
        print('NO')

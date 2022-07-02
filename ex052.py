num = int(input('Digite um número: '))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m',end=' ')
    print('{}'.format(c),end=' ')

if total == 2:
    print('\n\033[mO número {} é divisível apenas por 1 e por ele mesmo.'.format(num))
    print('O número {} \033[32mÉ PRIMO\033[m.'.format(num))
else:
    print('\n\033[mO número {} foi divisível {} vez(es) além de 1 e ele mesmo.'.format(num, total-2))
    print('O número {} \033[31mNÃO É PRIMO\033[m.'.format(num))
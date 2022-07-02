#tabuada
print('\033[35m-=-'*12)
print('{:~^36}'.format('TABUADA'))
print('\033[35m-=-\033[m'*12)

num = int(input('Digite um número: '))
for c in range (0,11):
    print('\033[32m{}\033[m x {:2} = \033[31m{}\033[m'.format(num, c, num*c))
#comparando número

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('\nO \033[35mprimeiro\033[m número é maior.')
elif num1 < num2:
    print('\nO \033[35msegundo\033[m número é maior.')
else:
    print('\nOs números são \033[35miguais\033[m.')
#menu de opções calculadora
from time import sleep
opção = 0
print('\033[35mCALCULADORA\033[m')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

while opção != 5:
    print('[1] somar\n[2] multiplicar\n[3] maior, menor ou igual?\n[4] digitar novos números\n[5] sair')
    opção = int(input('O que deseja fazer? '))


    if opção == 1:
        print('\033[32m{} + {} = {}\033[m'.format(num1,num2,num1+num2))
        print('-=-'*15)
        sleep(1)

    elif opção == 2:
        print('\033[32m{} x {} = {}\033[m'.format(num1,num2,num1*num2))
        print('-=-' * 15)
        sleep(1)

    elif opção == 3:
        if num1 > num2:
            print('\033[32m{} > {}\033[m'.format(num1,num2))
            print('-=-' * 15)
            sleep(1)
        elif num1 < num2:
            print('\033[32m{} < {}\033[m'.format(num1,num2))
            print('-=-' * 15)
            sleep(1)
        else:
            print('\033[32m{} = {}\033[m'.format(num1,num2))
            print('-=-' * 15)
            sleep(1)

    elif opção == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        print('-=-' * 15)
        sleep(1)

    elif opção == 5:
        print('\033[36mFinalizando...\033[m')
        sleep(1)

    else:
        print('\033[31mOpção inválida\033[m. Tente novamente...')
        print('-=-' * 15)
        sleep(1)



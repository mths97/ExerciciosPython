#conversor de base decimal

numero = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão:\n[1] Binário\n[2] Octal\n[3] Hexadecimal')

opção = int(input('Digite sua opção: '))

if opção == 1:
    print('O número {} em binário é: \033[32m{}\033[m.'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('O número {} em octal é: \033[32m{}\033[m.'.format(numero,oct(numero)[2:]))
elif opção == 3:
    print('O número {} em hexadecimal é: \033[32m{}\033[m.'.format(numero,hex(numero)[2:]))
else:
    print('Opção inválida.')
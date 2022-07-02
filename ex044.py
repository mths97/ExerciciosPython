#gerenciador de pagamentos
print('{:=^40}'.format(' CAIXA '))
preço = float(input('Valor a ser pago: '))

print('\n[1] à vista (dinheiro)\n[2] à vista (cartão)\n[3] em até 2x \n[4] 3x ou mais')
opção = int(input('Escolha a \033[35mCONDIÇÃO DE PAGAMENTO\033[m: '))

if opção == 1:
    preço = preço - (preço*10)/100
    print('\nPreço total: \033[32mR${}'.format(preço))
elif opção == 2:
    preço = preço - (preço*5)/100
    print('\nPreço total: \033[32mR${}'.format(preço))
elif opção == 3:
    print('\nPreço total: \033[32mR${}'.format(preço))
elif opção == 4:
    preço = preço + (preço*20)/100
    print('\nPreço total: \033[32mR${}'.format(preço))
else:
    print('\033[31m\nOpção inválida\033[m')
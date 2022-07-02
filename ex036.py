#aprovando empréstimo: se a prestação mensal for > que 30% do salário o empréstimo é negado

valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do comprador? '))
ano = int(input('Em quantos anos irá pagar? '))

prestação = valor / (ano * 12)

print('A prestação será de R${:.2f}'.format(prestação))
if prestação > (salario * 30)/100:
    print('Empréstimo \033[0;31mNEGADO\033[m.')
else:
    print('Empréstimo \033[0;32mAPROVADO\033[m.')
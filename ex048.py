#soma de todos os números ímpares múltiplos de 3 (de 1 até x)
soma = 0
contador = 0
ult = int(input('Digite o último número: '))
for c in range(1,ult+1):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
        contador += 1

print('\n\033[34m{}\033[m números foram encontrados.'.format(contador))
print('A soma dos números é \033[31m{}\033[m.'.format(soma))
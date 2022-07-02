#alistamento militar
from datetime import date
atual = date.today().year

nasc = int(input('Digite ano de nascimento: '))
idade = atual - nasc

print('Você tem {} anos em {}.'.format(idade,atual))

if idade == 18:
    print('Você pode se alistar!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Você só poderá se alistar em {].'.format(ano))
else:
    saldo = idade - 18
    ano = atual - saldo
    print('Você deveria ter se alistado em {}.'.format(ano))
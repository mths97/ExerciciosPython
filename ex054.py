#grupo da maioridade
from datetime import date
atual = date.today().year
maiores = 0
menores = 0

for c in range(1,8):
    ano = int (input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    idade = atual - ano
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print('\n{} pessoas são maiores de idade.'.format(maiores))
print('{} pessoas são menores de idade.'.format(menores))

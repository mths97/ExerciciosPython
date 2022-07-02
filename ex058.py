#adivinhação de número
from random import randint
erros = 0
computador = randint(1,10)
print('\033[1mAcabei de pensar em um número entre 1 e 10. Tente adivinhar...')
palpite = int(input('Qual seu palpite?\033[m '))

while computador != palpite:
    palpite = int(input('\033[31mVocê errou.\033[m Tente novamente: '))
    erros += 1

print('\033[32mVocê acertou!\033[m O computador pensou {}!!!'.format(computador))
print('\nNúmero de tentativas: {}'.format(erros+1))
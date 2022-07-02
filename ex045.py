#pedra, papel e tesoura
from random import randint
print('\033[33m{:=^40}\033[m'.format(' PEDRA, PAPEL E TESOURA '))

itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print ('[0] Pedra\n[1] Papel\n[2] Tesoura')
jogador = int(input('Escolha sua opção: '))

print('-=-'*10)
print('Você escolheu \033[33m{}\033[m.'.format(itens[jogador]))
print('O computador escolheu \033[33m{}\033[m.'.format(itens[computador]))
print('-=-'*10)

if computador == 0: #pedra
    if jogador == 0:
        print('\033[34mEMPATE\033[m')
    elif jogador == 1:
        print('Você \033[32mVENCEU\033[m')
    elif jogador == 2:
        print('Você \033[31mPERDEU\033[m')

elif computador == 1: #papel
    if jogador == 0:
        print('Você \033[31mPERDEU\033[m')
    elif jogador == 1:
        print('\033[34mEMPATE\033[m')
    elif jogador == 2:
        print('Você \033[32mVENCEU\033[m')

elif computador == 2: #tesoura
    if jogador == 0:
        print('Você \033[32mVENCEU\033[m')
    elif jogador == 1:
        print('Você \033[31mPERDEU\033[m')
    elif jogador == 2:
        print('\033[34mEMPATE\033[m')
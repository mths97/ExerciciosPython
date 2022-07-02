#classificando atletas
from datetime import date
nasc = int(input('Digite o ano de nascimento do atleta: '))

atual = date.today().year
idade = atual - nasc

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Categoria: \033[32mMIRIM\033[m.')
elif idade <= 14:
    print('Categoria: \033[32mINFANTIL\033[m')
elif idade <= 19:
    print('Categoria: \033[32mJUNIOR\033[m')
elif idade <= 25:
    print('Categoria: \033[32mSÊNIOR\033[m')
else:
    print('Categoria: \033[32mMASTER\033[m')
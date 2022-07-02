#avaliador genero
genero = str(input('Digite seu gênero(M/F): ')).upper()

while genero != 'M' and genero != 'F':
    genero = str(input('\033[31mDado inválido!\033[m\nDigite seu gênero(M/F): ')).upper()

if genero == 'M':
    print('\033[32mMasculino\033[m')
else:
    print('\033[32mFeminino\033[m')
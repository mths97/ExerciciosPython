#analisando triângulos

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\nAs retas \033[32mPODEM\033[m formar triângulo.')
    if r1 == r2 == r3:
        print('O triângulo é \033[34mEQUILÁTERO\033[m.')
    elif r1 != r2 != r3 and r1 != r3:
        print('O triângulo é \033[34mESCALENO\033[m.')
    else:
        print('O triângulo é \033[34mISÓCELES\033[m.')
else:
    print('\nAs retas \033[31mNÃO PODEM\033[m formar triângulo.')
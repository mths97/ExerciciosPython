#média

nota1 = float(input('Digite primeira nota: '))
nota2 = float(input('Digite segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('\nMédia: {}\nVocê foi \033[32mAPROVADO\033[m.'.format(media))
elif 5 <= media < 7:
    print('\nMédia: {}\nVocê está de \033[33mRECUPERAÇÃO\033[m.'.format(media))
else:
    print('\nMédia:{}\nVocê foi \033[31mREPROVADO\033[m.'.format(media))
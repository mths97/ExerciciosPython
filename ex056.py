#analisador completo (mostrar media, homem mais velho, numero de mulheres com menos de 20 anos)
soma = 0
hmaisvelho = 0
nomevelho = ''
fmenosvinte = 0

for c in range(1,5):
    print('----- {}ª Pessoa -----'.format(c))
    nome = str(input('Nome: ')).capitalize()
    idade = int(input('Idade: '))
    genero = str(input('Gênero (M/F): ')).upper()
    soma += idade
    if c == 1 and genero == 'M':
        nome = nomevelho
        hmaisvelho = idade
    else:
        if genero == 'M' and idade > hmaisvelho:
            hmaisvelho = idade
            nomevelho = nome
    if genero == 'F' and idade < 20:
        fmenosvinte += 1

media = soma / 4
print('\nA média de idade do grupo é: {}'.format(media))
print('O homem mais velho se chama {} e tem {} anos.'.format(nomevelho,hmaisvelho))
print('São {} mulheres com menos 20 anos.'.format(fmenosvinte))



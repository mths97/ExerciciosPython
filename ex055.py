#maior e menor da sequencia
maior = 0
menor = 0
for c in range(1,6):
    peso = int(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('\nMaior peso: {}Kg.\nMenor peso: {}Kg.'.format(maior,menor))
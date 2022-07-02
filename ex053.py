#detector de palíndromo
frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

print('\nVocê digitou a frase: {}.'.format(frase))
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso é: {}.'.format(inverso))

if inverso == junto:
    print('É um \033[32mPALÍNDROMO\033[m!!')
else:
    print('Não é um palíndromo.')

# separa-se a frase em palavras e depois junta as palavras sem os espaços (salva na variável junto)
# o laço for lê a palavra de trás pra frente e salva na variável inverso
# é um palíndromo se inverso e junto forem iguais

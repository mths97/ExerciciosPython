#calculadora de IMC

peso = float(input('Digite seu peso (em Kg): '))
altura = float(input('Digite sua altura (em m): '))
imc = peso / pow(altura,2)

print('\nIMC: {:.1f}'.format(imc))

if imc < 18.5:
    print('\033[36mABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('\033[35mPESO IDEAL')
elif 25 <= imc < 30:
    print('\033[34mSOBREPESO')
elif 30 <= imc < 40:
    print('\033[33mOBESIDADE')
else:
    print('\033[31mOBESIDADE MÓRBIDA')
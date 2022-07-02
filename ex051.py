#progressão aritmética

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão #fórmula matemática

for c in range(primeiro, décimo+razão, razão):
    print('{}'.format(c),end=' ')
print(';')
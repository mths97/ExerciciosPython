#contagem regressiva (10 até 0) com intervalo de 1 segundo
from time import sleep
for cont in range (10,-1,-1):
    print(cont)
    sleep(1)
print('Fim.')
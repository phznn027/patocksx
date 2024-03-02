import random 
import time 

lista_numeros = ['0', '1', '2', '3', '4', '5']

numero_aleatorio = int(random.choice(lista_numeros))

print('Aguarde...\nPensando em um numero!')
time.sleep(1)
adivinha = int(input('Tente adivinha qual o numero que o computador pensou?'))
print('PROCESSANDO')
time.sleep(1)


if adivinha == numero_aleatorio:
    print(f'Voce acertou, pois o numero que o computador pensou foi {numero_aleatorio}')
else:
    print(f'Voce errou, pois o numero que o computador pensou foi {numero_aleatorio}')

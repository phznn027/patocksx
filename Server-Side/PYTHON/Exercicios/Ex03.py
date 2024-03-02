velocidade = int(input('Qual e a velocidade do carro: '))
velocidade_max = 80

if velocidade > velocidade_max:
    print(f'Voce sera multado pois passou do limite de 80km/h, voce esta a {velocidade}Km/h')
elif velocidade == velocidade_max:
    print(f'Voce esta no limite da velocidade maxima, mas o gerente esta maluco e decidiu nao te multa dessa vez!')
else:
    print(f'voce esta abaixo do limite maximo parabens, voce esta a {velocidade}km/h')

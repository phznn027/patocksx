altura = float(input('Informe sua altura (Kg): '))
peso = float(input('Informe seu peso (m): '))

imc = peso / (altura * altura)
imc = imc
print(f'O seu imc é {imc:.1f}')

if imc < 18.5:
    print('Voce esta abaixo do peso!.')
    print('Comece a comer mais!!!.')

elif imc >= 18.5 and imc < 25:
    #elif 18.5 <= imc < 25:
    print('Voce esta no peso ideal.')
    print('Parabens continue assim!.')

elif imc >= 25 and imc < 30:
    print('Voce esta acima do peso!!.')
    print('Pare de comer retardado(a)!.')

elif imc >= 30 and imc < 40:
    print('Voce esta obso.')
    print('Bora fazer uma dieta ne pai? madeira esta caro!.')

elif imc >= 40:
    print('Voce agora esta com obsidade morbida!.')
    print('Se fudeu avisei para parar de comer, e fazer uma dieta!.')
    print('Agora so vai da despesar com caixao, fdp')
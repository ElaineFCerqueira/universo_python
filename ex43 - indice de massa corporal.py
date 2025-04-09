#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) 
# e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

import os
os.system('cls||clear')

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso/(altura**2)

if imc < 18.5:
    print(f', IMC {imc} - Abaixo do peso')
elif imc <= 25:
    print(f'IMC {imc} - Peso Ideal')
elif imc <= 30:   
    print('IMC {} - Sobrepeso '.format(imc))
elif imc <= 40:
    print(f'IMC {imc} - Obesidade')
else:
    print(f'IMC {imc} - Quilos mortais') 
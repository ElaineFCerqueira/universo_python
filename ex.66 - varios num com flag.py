'''
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

'''

import os
os.system('cls||clear')

quant = soma = 0

while True:
    num = int(input('Digite um numero: '))
        
    if num == 999:
        break
    quant+=1
    soma+=num
print(f'Você digitou {quant} numeros e a soma é {soma}')
    
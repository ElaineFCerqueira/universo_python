'''Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''


import os
os.system('cls||clear')

num = contador = soma = 0
num = int(input('Digite um valor: [999 para parar]: '))

while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um valor: [999 para parar]: '))
print(f'Você digitou {contador}, e a soma ficou {soma} ')
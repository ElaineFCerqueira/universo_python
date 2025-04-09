'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

import os
os.system('cls||clear')
# num = 0
# resp = 'S'
# soma = quant = media = 0
# if quant == 1:
#     maior == menor = num

# while resp in 'Ss':
#     num = int(input('Digite um numero: '))
#     soma += num
#     quant += 1                                                               
    
    
#     resp = input('Deseja continuar? [S/N]') .upper().strip()[0]  #.upper() coloca em maiuscula
# media = soma / quant                                             #.strip()  remover os espaços
#                                                                  #[0] considerar só a primeira letra
# print(f'Você digitou {quant} numeros e a soma: {soma}')

resp = 'S'
quant = 0
soma = 0
maior = 0
menor = 0

while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant +=1 
    if quant == 1:
        maior == menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
    resp = input('Deseja continuar? ')
media = soma/quant
print('Acabou!!!')
print(f'Você digitou {quant} numeros, A soma dos valores é {soma}, e a média é {media}')
print(f'O maior nummero é {maior} e o menor numero é {menor}')
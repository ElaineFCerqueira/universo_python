'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e 
também indique o menor e o maior valor que estão na tupla.'''

import os
os.system('cls||clear')

from random import randint

numero = randint(1, 60),randint(1, 60), randint(1, 60), randint(1, 60),randint(1, 60),randint(1, 60)
print(f'Os valores sorteados são: {sorted(numero)}')

print(f'O maior valor sorteado foi : {max(numero)}')
print(f'O menor valor sorteado foi : {min(numero)}')

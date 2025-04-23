
#Crie um programa que leia um número inteiro 
#e mostre na tela se ele é PAR ou ÍMPAR.
import os
os.system('cls||clear')

num = int(input('Digite um numero: '))

if num % 2 == 0:
    print(f'Esse numero {num} é par')
else:
    print(f'O numero {num} é impar')

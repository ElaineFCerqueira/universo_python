# Faça um programa que leia um número inteiro e 
# diga se ele é ou não um número primo.

import os
os.system('cls||clear')

#função

def num_primo(numero):
    if numero <= 1:
        print('Não é numero primo')
    
    for c in range(2,numero//2):
        if numero % c == 0:
            return('Não é numero primo')
    else:
        return('O numero é primo')







numero = int(input('Digite um numero: '))

resultado = num_primo(numero)

print(f' {numero}, É primo? {resultado}' )



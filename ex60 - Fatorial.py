#Faça um programa que leia um número qualquer e mostre o seu fatorial.

#USANDO MODULO

#from math import factorial
#n = int(input('Digite um numero: '))
#f = factorial(n)
#print(f'O fatorial de {n} é {f}')

#SEM MODULO

n = int(input('Digite um numero: '))
contador = n
fatorial = 1

while contador > 0:
    print(f'{contador}', end='')

    print(' x ' if contador > 1 else ' = ', end='')

    fatorial *= contador

    contador-=1

print(f'{fatorial}')    
'''
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.
'''
import os
os.system('cls||clear')

valores = []
pares = []
impares = []

while True:
    numero = (int(input('Digite um numero: ')))
    valores.append(numero)

    continuar = input('Deseja continuar? (S/N): ')
    if continuar in 'Nn':
        break
print(f'Os numeros digitados foram: {valores}')

for i , v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
    
print(f'Par: {pares}')
print(f'Impares: {impares}')

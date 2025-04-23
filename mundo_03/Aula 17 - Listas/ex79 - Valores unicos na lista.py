'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

import os
os.system('cls||clear')


lista = []

while True:
    numero = int(input('Digite um numero: '))
    if numero not in lista:
        lista.append(numero)
        print('Adicionado com sucesso.')

    else:
        print('Numero duplicado, tente novamente')
        
    
    continuar = input('Deseja continuar? (S/N) ').strip().upper()[0]
    if continuar in 'Nn':
        break
lista.sort()    
print(f'Você digitou os numeros: {lista}')

    

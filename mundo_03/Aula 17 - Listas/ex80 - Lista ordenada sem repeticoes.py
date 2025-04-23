'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''
import os
os.system('cls||clear')

lista = []

for contador in range (0,5):
    numero = int(input('Digite um numero: '))
    if contador == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos,numero)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos +=1
print(f'Os valores digitados são: {lista}') 
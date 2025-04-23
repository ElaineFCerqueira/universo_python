'''
Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas. 
B) Uma listagem com as pessoas mais pesadas.                                                                                                   
C) Uma listagem com as pessoas mais leves.
'''
import os
os.system('cls||clear')

lista = []
dados = []

while True:
    dados.append(input('Digite o nome: '))
    dados.append(int(input('Digite o peso: ')))
    lista.append(dados[:])
    dados.clear()
    
    resposta = input('Deseja continuar? (S/N): ') .strip() .upper()[0]
    if resposta in 'Nn':
        break

print(lista)
print(f'Foram {len(lista)} pesssoas cadastradas')

for p in lista:
    if p[1] >= 100:
        print(f'{p[0]} está acima do peso')
    else:
        print(f'{p[0]} está abaixo do peso')
'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
import os
os.system('cls||clear')

valores = []

for i in range (0,5):
    valores.append(int(input('Digite um valor: ')))
    
print(f'Os valores foram: {valores}')

print(f'Maior valor: {max(valores)} na posição: ', end= '')
for c, v in enumerate(valores):
    if v == max(valores):
        print(f'{c+1}', end='...')



print(f'Menor valor: {min(valores)} na posição: ', end= '')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f'{c+1}', end='...')
    

# print(f'Menor valor: {min(valores)} na posição {c}')

# lote = []

# for contador in range(0,5):
#     lote.append(int(input('Digite um numero: ')))
# print(lote)
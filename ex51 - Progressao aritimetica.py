# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

import os
os.system('cls||clear')

#for pa in range (0,20,2):
#    print(pa,end=' - ')
#print('ACABOU')

primeiro = int(input('Digite primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10-1)*razao

for pa in range(primeiro,decimo+razao,razao):
    print(f'{pa}', end=' - ' )
print('ACABOU')
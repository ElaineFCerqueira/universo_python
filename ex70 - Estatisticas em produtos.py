import os
os.system('cls||clear')

'''
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''
total = 0
totalprod = 0
totmil = 0
menor = 0
cont = 0
barato = ' '

while True:
    produto = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: R$ '))
    cont+=1
    total +=valor
    if valor > 1000:
        totmil+=1
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
        
    
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]: ').strip() .upper()[0]
    if continuar == 'N':
        print('Finalizando...')
        break
print(f'O valor total das compras foi de R$ {total:.2f}')  
print(f'Temos {totmil} produto custando mais de R$ 1.000 ')  
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')    
    
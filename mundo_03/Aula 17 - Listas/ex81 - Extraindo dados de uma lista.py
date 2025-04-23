'''
 Crie um programa que vai ler vários números e colocar em uma lista.                  
 Depois disso, mostre: 
 A) Quantos números foram ditados        
 B) A lista de valores, ordenada de forma decrescente.  
 C) Se o valor 5 foi digitado e está ou não na lista.
'''
import os
os.system('cls||clear')

lista = []

while True:
    numero = int(input('Digite um numero: '))
    lista.append(numero)

    resposta = input('Deseja continuar (S/N)?  ') .strip().upper()[0]
    if resposta in 'Nn':
        break

print(f'A lista possuem {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os numero digitados foram: {lista}')
if 5 in lista:
    print('O numero 5 faz parte da lista')
else: 
    print('O numero 5 não faz parte da lista')
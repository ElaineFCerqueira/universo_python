#Desenvolva um programa que leia o comprimento de três retas 
#e diga ao usuário se elas podem ou não formar um triângulo.
import os
os.system('cls||clear')

print('='*30)
print('ANALISADOR DE TRIÂNGULOS')
print('='*30)

a = float(input('Digite um numero: '))
b = float(input('Digite um numero: '))
c = float(input('Digite um numero: '))

if a < b + c and b < a + c and c < a + b :
    print('Essas medidas podem formar um triângulo')
else:
    print('Nesses medidas não podem formar triângulo')

import os
os.system('cls||clear')

#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

reta1 = float(input('Digite um numero: '))
reta2 = float(input('Digite um numero: '))
reta3 = float(input('Digite um numero: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os elementos acima podem formar um triângulo')

    if reta1 == reta2 == reta3:
        print('É um triangulo Equilatero')

    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('É um triângulo Isósceles')
    
    elif reta1!=reta2 or reta2!=reta3 or reta3!=reta1:
        print('É um triângulo Escaleno')

else:
    print('Não pode formar um triângualo')
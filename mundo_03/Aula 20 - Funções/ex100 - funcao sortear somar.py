'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar 
a soma entre todos os valores pares sorteados pela função anterior.
'''
from random import randint
from time import sleep

def sorteia(lista):
    for cont in range (0,5):
        n = randint(1,10)
        lista.append(n)
        print(n,end=' ', flush='True')
        sleep(0.3)
    print('Pronto!')

def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores da lista temos {soma}')



#Programa Principal
numeros = list()
sorteia(numeros)
soma_par(numeros)
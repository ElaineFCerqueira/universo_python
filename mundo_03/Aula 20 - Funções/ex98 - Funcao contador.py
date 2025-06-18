import os
os.system('cls||clear')

from time import sleep


'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:            
a) de 1 até 10, de 1 em 1 
b) de 10 até 0, de 2 em 2       
c) uma contagem personalizada
'''

def contador(i,f,p):
    if i<f:
        cont = i
        while cont <= f:
            print(cont,end=' ',flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(cont,end=' ',flush=True)
            sleep(0.5)
            cont-=p
        print('FIM')         


#Programa Principal
contador(1,10,2)
contador(10,0,2)
print('Agora é sua vez de personalizar ')
inicio = int(input('Digite um inicio:'))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
contador(inicio,fim,passo)
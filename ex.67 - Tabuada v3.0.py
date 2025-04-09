'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.
'''

import os
os.system('cls||clear')




while True:
    numero = int(input('Deseja ver a tabuada de que valor? '))
    if numero < 0:
        break
    else:
        for contador in range(0,10):
            multiplicacao = (contador+1)*numero
            print(f'{numero} x {contador+1} = {multiplicacao}')
print('PROGRAMA TABUADA ENCERRADO...')
    
    
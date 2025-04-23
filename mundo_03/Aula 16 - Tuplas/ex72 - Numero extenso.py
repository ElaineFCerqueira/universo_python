'''Crie um programa que tenha uma tupla totalemte preenchida 
com uma contagem por extenso de zero até vinte.
Digite um numero entre 0 e 20 '''

import os
os.system('cls||clear')

cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')



while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente Novamente ')
print(f'Você digitou o numero: {cont[num]}')    

continuar = ' '
while continuar not in 'SN':
    continuar = input('Deseja continuar? [S/N]: ').strip() .upper()[0]
    if continuar == 'S':
        num = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente Novamente ')
    elif continuar == 'N':
        print('Finalizando...')
        break
print(f'Você digitou o numero: {cont[num]}')    
'''
Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues. 
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
import os
os.system('cls||clear')

print('='*40)
print('{:^40}'.format('BANCO ZUVINHA'))
print('='*40)

valor = int(input('Qual o valor deseja sacar R$: '))
total = valor
cedula = 50
totced = 0

while True:
    if total >=cedula:
        total-=cedula
        totced+=1
        
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R$ {cedula} ')
        if cedula == 50:
            cedula = 20
            
        elif cedula == 20:
            cedula = 10
            
        elif cedula == 10:
            cedula = 1
            
        totced = 0
        if total == 0:
            break    
            
        


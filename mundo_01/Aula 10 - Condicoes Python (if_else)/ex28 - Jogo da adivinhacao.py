#Escreva um programa que faça o computador “pensar” em um 
#número inteiro entre 0 e 5 e peça para o usuário tentar 
#descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
import os
import time 
os.system('cls||clear')

#computador = randint(0,5) faz o computador pensar no numero entre 0 e 5

lista = [0,1,2,3,4,5]
escolhido = random.choice(lista)

num = int(input('Escolha um numero entre 0 e 5: '))
print(' PROCESSANDO...')
time.sleep(2)

if num == escolhido:
    print(f'Você acertou!!! o numero escolhido foi {escolhido}')
elif num > 5:
    print('Escolha um numero válido entre 0 e 5')
else:
    print(f'COMPUTADOR: EU GANHEI!!! Pensei no numero: {escolhido} ')
print('--- FIM ---')

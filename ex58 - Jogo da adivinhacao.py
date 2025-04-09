#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
#Só que agora o jogador vai tentar adivinhar até acertar, 
#mostrando no final quantos palpites foram necessários para vencer.
import os
from random import randint 

os.system('cls||clear')



computador = randint(0,10)
print('Sou computador acabei de pensar em um numero entre 0 e 10')
print('Será que você consegue adivinhar?! ')

palpite = 0
acertou = False

while not acertou:
    jogador = int(input('Digite seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
        print(f'Acertou!!! Com tantos {palpite} palpites')
    else:
        if jogador > computador:
            print('Huum, tá frio. É menor')
        elif jogador < computador: 
            print('O numero é maior')

#Crie um programa que faça o computador jogar Jokenpô com você.
#regra: A pedra quebra a tesoura, a tesoura corta o papel e o papel embrulha a pedra
import os
from random import randint
import time
os.system('cls||clear')


itens = ('Pedra', 'Papel','Tesoura')

computador = randint(0,2) #gera numeros aleatórios
print(''' Sua opções:
      [0] Pedra
      [1] Papel
      [2] Tesoura
    ''')
Jogador = int(input('Digite sua jogada: '))
print('-'*30)
print('O computador escolheu {}'.format(itens[computador]))
print('O Jogador escolheu {}'.format(itens[Jogador]))
print('-'*30)
print('-'*30)
if computador == 0:
    if Jogador == 0:
        print('Jogo empatado')
    elif Jogador == 1:
        print('O Jogador ganhou!!!')
    elif Jogador == 2:
        print('O computador ganhou!!!')
elif computador == 1:
    if Jogador == 0:
        print('O Computador Ganhou!!')
    elif Jogador == 1:
        print('Jogo empatado. Tente novamente')
    elif Jogador == 2:
        print('O jogador ganhou!!')
elif computador == 2:
    if Jogador == 0:
        print('O Jogador ganhou!')
    elif Jogador == 1:
        print('O Computador ganhou!')
    elif Jogador == 2:
        print('Jogo empatado, tente novamente')
else:
    print('Opção Inválida, tente novamente'  )
'''
Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
import os
from random import randint

os.system('cls||clear')
v=0
while True:
    jogador = int(input('Diga um valor? '))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Impar [P/I]?').strip() .upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v+=1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu')
            v+=1
        else:
            print('Você perdeu!!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!!! Você venceu {v} vezes')

            





# num = int(input('Escolha um numero entre 0 e 5: '))
# print(' PROCESSANDO...')
# time.sleep(2)

# if num == escolhido:
#     print(f'Você acertou!!! o numero escolhido foi {escolhido}')
# elif num > 5:
#     print('Escolha um numero válido entre 0 e 5')
# else:
#     print(f'COMPUTADOR: EU GANHEI!!! Pensei no numero: {escolhido} ')
# print('--- FIM ---')

# if num % 2 == 0:
#     print(f'Esse numero {num} é par')
# else:
#     print(f'O numero {num} é impar')
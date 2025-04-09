import os
from datetime import date
os.system('cls||clear')

# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.


def logo_senai():
    print('==== CURSO EM VÍDEOS ==== ')

def ano(nascimento):
    atual = date.today().year
    totalmaior = 0
    totalmenor = 0
    for pessoa in range (1,8):
        nascimento = int(input('Digite seu o ano de nascimento: '))
        idade = atual - nascimento
        if idade >=21:
            totalmaior +=1
            
        else:
            totalmenor +=1
    print(f'{pessoa}')
    print(f'Ao todo tivemos {totalmaior} pessoas maiores de idade')
    print(f'Ao todo tivemos {totalmenor} pessoas menores de idade')







logo_senai()
nascimento = int(input('Digite seu o ano de nascimento: '))
ano(nascimento)





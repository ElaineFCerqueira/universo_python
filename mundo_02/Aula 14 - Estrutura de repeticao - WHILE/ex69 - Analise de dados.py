'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

import os
os.system('cls||clear')

tot18 = totH = totM20 = 0

while True:
    idade = int(input('Digite uma idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Qual o sexo [M/F]: ').strip() .upper()[0]
    if idade >=18:
        tot18+=1
    if sexo == 'M':
        totH+=1
    if sexo == 'F' and idade < 20:
        totM20+=1
    
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N]: ').strip() .upper()[0]
    if resp == 'N':
        break
print(f'Pessoas tem mais de 18 anos são {tot18}')
print(f'Homens cadastrados são: {totH}')
print(f'Mulheres tem menos de 20 anos são {totM20}')
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

import os
os.system('cls||clear')

#def logo():
#    print(f'==== {i}ª pessoa ===')


soma_idade = 0
media = 0
mais_velho = 0
nome_velho = ''
total_mulh20 = 0
for p in range(1,5):
    print(f'---- {p}º pessoa ----')
    
    nome = input('Digite o nome: ').strip() #juntar o nome
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: (M / F): ').upper() #upper coloca em maiuscula
    
    soma_idade+= idade

  
    if p == 1 and sexo in 'Mm':
        mais_velho = idade
        nome_velho = nome 
    if sexo in 'Mm' and idade > mais_velho:
        mais_velho = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulh20+=1
    

media = soma_idade/4
print(f'A média das idade  do grupo é {round(media,0)} anos' )
print(f'O homem mais velho tem {mais_velho} anos e se chama {nome_velho}')
print(f'O total de mulheres com menos de 20 anos é {total_mulh20}')
#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

import os
os.system('cls||clear')

sexo = input('Digite o seu sexo (M/F): ').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Dados invalidos, Digite o seu sexo (M/F): ').strip().upper()[0]
print('Sexo registrado com sucesso')
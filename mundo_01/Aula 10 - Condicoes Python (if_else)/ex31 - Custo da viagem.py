#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
import os
os.system('cls||clear')

cidade = int(input('Para qual cidade pretende viajar? '))
if cidade <= 200:
    passagem = (200-cidade)*0.50
    print(f'Para {cidade}Km, você pagará R$ {passagem} reais em passagem')
else:
    passagem = (cidade - 200)*0.45
    print(f'Para {cidade}Km, você pagará R$ {passagem} reais em passagem')

print('Tenha uma boa viagem!!')

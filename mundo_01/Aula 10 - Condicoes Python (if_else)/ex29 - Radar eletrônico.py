#Escreva um programa que leia a velocidade de um carro. 
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
#A multa vai custar R$7,00 por cada Km acima do limite.
import os
os.system('cls||clear')


vel = int(input('Qual a sua velocidade? '))
if vel > 80:
    multa = 7*(vel-80)
    print(f'Você excedeu a velocidade, a multa será de R$ {multa} reais')
else:
    print('Tenha uma boa viagem, dirija com segurança')

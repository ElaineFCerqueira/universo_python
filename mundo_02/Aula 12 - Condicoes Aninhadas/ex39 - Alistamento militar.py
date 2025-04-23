#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar,
#  se é a hora exata de se alistar 
# ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import os
os.system('cls||clear')

nasc = int(input('Digite o ano que você nasceu? '))
idade = 2024 - nasc

if idade < 18:
    a = 18 - idade
    print(f'Sua idade para alistamento ainda chegou, faltam {a} anos')

elif idade == 18:
    print('Você está no ano exato para o alistamento')

else:
    b = idade - 18
    print(f'Você perdeu seu prazo de seu alistamento, você está {b} anos atrasado')


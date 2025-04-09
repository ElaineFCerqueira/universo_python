import os
os.system('cls|| clear')

#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

def logo_curso():
    print('==== Curso em video ===')


def calculo_peso(peso):
    maior_peso = 0
    menor_peso = 0
    for pessoa in range(2,6):
        #peso = float(input(f'Informe qual o seu peso da {pessoa+1}º pessoa: '))
        peso = float(input(f'Informe qual o peso da {pessoa}º pessoa: '))
        maior_peso and menor_peso == 0
        if pessoa == 1:
            maior_peso == peso
            menor_peso == peso
        else:
            if peso > maior_peso:
                maior_peso = peso
            if peso < menor_peso:
                menor_peso = peso
    print(f'O Maior peso é : {maior_peso}')
    print(f'O Menor peso é : {menor_peso}')



logo_curso()

peso = float(input(f'Informe qual o peso da 1º pessoa: '))
calculo_peso(peso)














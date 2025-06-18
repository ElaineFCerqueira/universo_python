import os
os.system('cls||clear')

def titulo(msg):
    print(msg)
    print("-"*30)


def calculo(Largura,Comprimento):
    cal = Largura*Comprimento
    print(f'A area do terreno {Largura} x {Comprimento} = {cal} metros')
    

#Programa Principal
titulo('Controle de Terreno')
Largura= float(input('Digite a Largura: '))
Comprimento= float(input('Digite a Comprimento: '))
calculo(Largura,Comprimento)

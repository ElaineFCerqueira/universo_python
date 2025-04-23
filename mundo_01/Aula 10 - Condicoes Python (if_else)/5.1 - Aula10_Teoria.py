import os
os.system('cls||clear')

#Se carro.esq():
#Senão:

#if carro.esq():
#esle:


#exercicio
tempo = int(input('Quantos anos tem seu carro? '))

if tempo <=3:
    print('Seu carro é novo')
else:
    print('Humm, carro velhinho')
print('--- FIM ---')

#

nome = str(input('Qual o seu nome? '))
if nome == 'Gustavo':
    print(f'Que nome lindo!')
else: 
    print('Seu nome é tão normal')
print(f'Bom dia! {nome}')

#calculo de média

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi de : {m} ')

if m<5:
    print('você está reprovado')

elif m ==5 or m == 5.9:
    print('Você está na recuperação')

else:
    print('Você está aprovado')
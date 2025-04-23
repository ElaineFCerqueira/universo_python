#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

import os
os.system('cls||clear')

casa = float(input('Quanto custa a casa que deseja comprar? '))
sal = float(input('Qual o seu salario? '))
anos = int(input('Em quantos anos pretende pagar? '))

saldo_salario = sal*30/100
print(saldo_salario)

prest_mensal = casa/(anos * 12)


if prest_mensal <= saldo_salario:
    print('Seu empréstimo foi aprovado! ')
    print(f'A prestação mensal da casa será de {prest_mensal} reais')

else:
    print('Seu pedido de empréstimo foi negado.')
    print(f'Sua prestação é de {prest_mensal} e você tem disponivel {saldo_salario}')


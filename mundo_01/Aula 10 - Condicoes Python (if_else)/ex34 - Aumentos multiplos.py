#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. 
#Para os inferiores ou iguais, o aumento é de 15%.
import os
os.system('cls||clear')


salario = float(input('Qual o valor do seu salario? '))

if salario > 1250:
    aumento = (salario*10)/100
    novo_salario = salario + aumento
    print(f'Seu aumento foi de {aumento}, seu novo salario é de {novo_salario} reais')

else:
    salario <= 1250
    aumento = (salario*15)/100
    novo_salario = salario + aumento
    print(f'O seu aumento foi de {aumento}, seu novo salario será: {novo_salario} reais')
print('Tá feliz?! agora vá trabalhar!!')
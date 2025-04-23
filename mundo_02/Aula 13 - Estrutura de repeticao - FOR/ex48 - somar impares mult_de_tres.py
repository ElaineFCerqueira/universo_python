#Faça um programa que calcule a soma entre todos os números que são 
# múltiplos de três e que se encontram no intervalo de 1 até 500.
import os
os.system('cls||clear')


soma = 0 # acumulador soma o que tem
cont = 0 # contador soma +1

for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        #soma = soma + c
        soma+=c
print(f'A soma dos valores: é {soma}, e encontrou {cont} numeros')
#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.
import os
os.system('cls||clear')


num = int(input('Digite um numero inteiro: '))
print('''Menu de opções:
      [1] converter para Binário
      [2] converter para OCTAL
      [3] converter para Hexadecimal ''')
opcao = int(input('Digite a sua opção: '))

if opcao == 1:
    a = bin(num)
    print(f'O numero {num} convertido para binario, é {a}')
elif opcao == 2:
    b = oct(num)
    print(f'O numero {num} convertido para OCTAL, é {b}')
elif opcao == 3:
    c = hex(num)
    print(f'O numero {num} convertido para Hexadecimal, é {c}')
else:
    print('Opção invalida, tente novamente')
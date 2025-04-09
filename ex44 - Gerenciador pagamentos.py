# Elabore um programa que calcule o valor a ser pago por um produto, 
#  considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

import os
os.system('cls||clear')

produto = float(input('Digite qual o valor do produto R$:'))

print(''' Como deseja pagar?
      [1] Á vista
      [2] Credito ''')
opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    avista = produto*10/100
    print(f'O valor do seu desconto será de {avista}, seu total será de {produto-avista} reais')
    
elif opcao == 2:
    parc = int(input('Divide em quantas parcelas? '))
    
    if parc == 1:
        avista_cred = produto*5/100
        print(f'O valor do seu desconto será de  {avista_cred}, seu total será de {produto-avista_cred} reais ')

    elif parc == 2:
        cred = produto/2
        print(f'O valor do produto é de {produto} em duas parcelas de {cred} reais ')

    elif parc == 3:
        cred_juros = produto*20/100
        print(cred_juros)
        print(f'O valor do produto é de {produto} em {parc} parcelas de {(produto+cred_juros)/parc} reais')   



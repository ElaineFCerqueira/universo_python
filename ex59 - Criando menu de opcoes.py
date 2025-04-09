#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
import os
os.system('cls||clear')

primeiro_numero = int(input('Digite o primeiro valor: '))
segundo_numero = int(input('Digite o segundo valor: '))

opcao = 0
while opcao != 5:
    print('''\n Selecione uma das opções: 
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')

    opcao = int(input('Digite a opção desejada:'))

    if opcao == 1:
        soma = primeiro_numero + segundo_numero
        print(f'A soma de {primeiro_numero} + {segundo_numero} = {soma}')

    elif opcao == 2:
        mult = primeiro_numero*segundo_numero
        print(f'A multiplicação é {primeiro_numero} x {segundo_numero} = {mult}')
    
    elif opcao == 3:
        if segundo_numero > primeiro_numero:
            print(f'O {segundo_numero} é maior que {primeiro_numero}')
        else:
            print(f'O {primeiro_numero} é maior que {segundo_numero}')
    
    elif opcao == 4:
        novo_numero = input('Digite um novo numero:')
        print(f'{primeiro_numero}, {segundo_numero}, {novo_numero}')

    elif opcao == 5:
        print('Finalizando...')

    else:
        print('Opção inválida, tente novamante')
print('Fim do programa! volte sempre!')

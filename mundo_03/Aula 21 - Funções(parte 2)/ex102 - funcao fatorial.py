#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, 
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(n,show=False):
    f = 1
    for c in range (n,0,-1):
        # if show:
        #     print(c,end=' ')
        #     if c > 1:
        #         print('x' , end=' ')
        # else:
        #     print('=' , end='')
        f*=c
    print(f)

#Programa Principal
n = int(input('Digite um numero: '))
fatorial(n)    
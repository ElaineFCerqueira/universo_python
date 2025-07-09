#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro 
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa 
# tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições

from datetime import date

def voto(ano,ano_atual):
    idade = ano_atual - ano
    print(f'Você tem {idade} anos', end=" -> ")

    if idade >= 18 and idade <= 65:
        print('Voto OBRIGATÓRIO')
    elif idade <=15:
        print('Voto NEGADO')
    else:
        print('Voto OPCIONAL')


#Programa principal

ano_atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
voto(ano,ano_atual)
#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, 
#de acordo com a idade:
#– Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

import os
os.system('cls||clear')
ano_atual = 2024

nasc = int(input('Digite o ano do seu nascimento: '))
ano = ano_atual - nasc

if ano <= 9:
    print(f'Você tem {ano} anos, Sua categoria é a MIRIM')
elif ano <= 14:
    print(f'Você tem {ano} anos, Sua categoria é a INFANTIL') 
elif ano <=19:
    print(f'Você tem {ano} anos, Sua categoria é a JÚNIOR')
elif ano <=25:
    print(f'Você tem {ano} anos, Sua categoria é a SÊNIOR')
else:
    print(f'Você tem {ano} anos, Sua categoria é a MASTER')  
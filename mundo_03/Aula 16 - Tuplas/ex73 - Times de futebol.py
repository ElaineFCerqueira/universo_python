'''
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da 
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
'''

import os
os.system('cls||clear')


times = ('Botafogo', 'Palmeiras','Flamengo','Fortaleza','Internacional',
         'São Paulo','Corinthians','Bahia','Cruzeiro','Vasco',
         'Chapeonese','Atlético-MG','Fluminense','Grêmio','Juventude,'
         'Bragantino','Athletico-PR','Criciúma','Atlético-GO','Cuiabá')
print('-'*90)
print(f'A lista de time é : {times}')
print('-'*90)

#for t in times:
#    print(t)

print(f'Os cinco primeiros colocados são: {times[0:5]}')
print('-'*90)

print(f'Os quatros ultimos colocados são: {times[-4:]}')
print('-'*90)

print(f'A Chapeonese está na {times.index('Chapeonese')+1}ª posição')
print('-'*90)
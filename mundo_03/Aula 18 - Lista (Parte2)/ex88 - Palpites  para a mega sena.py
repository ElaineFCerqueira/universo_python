import os
os.system('cls||clear')

from random import randint
lista = []
contador = 0
total = 0
jogos = []

print('-'*50)
print(' '*10,'JOGO DA MEGA SENA')
print('-'*50)
quantidade = int(input('Quantos jogos você quer que eu sortei? '))
while total < quantidade:
    contador = 0
    while True:
        numero = randint(1,25)
        if numero not in lista:
            lista.append(numero)
            contador +=1
        if contador >= 6:
            break
    total += 1
    jogos.append(lista[:])
    lista.clear()
#print(f'Os numeros sorteados foram: {sorted(jogos)}\n')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
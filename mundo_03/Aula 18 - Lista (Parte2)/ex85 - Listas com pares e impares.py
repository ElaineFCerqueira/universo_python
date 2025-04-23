
import os
os.system("cls||clear")

lista = [[],[]]
for c in range(1,8):
    valor= (int(input('Digite um valor: ')))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(f'Os numeros pares foram: {sorted(lista[0])}')
print(f'Os numeros impares foram: {sorted(lista[1])}')
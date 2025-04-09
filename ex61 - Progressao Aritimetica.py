import os
os.system('cls||clear')

def logo():
    print('==== Curso em Video ====')


logo()
prim_termo = int(input('Digite um numero: '))
razao = int(input('Digite um razão da PA: '))
termo = prim_termo
cont = 1

while cont <=10:
    print(f'{termo}', end=' -> ')
    termo +=razao
    cont +=1
print('Fim')
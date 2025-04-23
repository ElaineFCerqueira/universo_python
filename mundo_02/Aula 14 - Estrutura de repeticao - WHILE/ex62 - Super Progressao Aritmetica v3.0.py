import os
os.system('cls||clear')

def logo():
    print('==== Curso em Video ====')


logo()
prim_termo = int(input('Digite um numero: '))
razao = int(input('Digite um razão da PA: '))
termo = prim_termo
cont = 1
total = 0
mais = 10

while mais !=0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end=' -> ')
        termo +=razao
        cont +=1
    print('Pausa')
    mais = int(input('Quantos mais deseja mostrar? '))
print(f'Progressão finalizada com {total} termos mostrados')
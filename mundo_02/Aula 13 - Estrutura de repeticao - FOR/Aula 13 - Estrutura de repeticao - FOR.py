import os
os.system('cls||clear')

for c in range(1,10): #conta de 1 até 10
    print(c)


for c in range(0,6): #repete o nome de 6 vezes
    print('Oi')
print('Fim')


for c in range(6,0,-1): #conta na ordem decrescente
    print(c)


for c in range(0,7,2): #conta de 0 a 7 pulando de 2 em 2,
    print(c)    


n = int(input('Digite um numero: '))
for c in range(0,n+1):
    print(c)


i = int(input('Inicio: '))
f = int(input('FIM: '))
p = int(input('Passo: '))
for c in range(i,f+1,p):
    print(c)


for c in range(0,3):
    n = int(input('Digite um numero'))
print('Fim')  


s=0
for c in range(0,4):
    n = int(input('Digite um numero: '))
   # s = s+n ou
    s+=n
print(f'A soma dos valores é {s}')
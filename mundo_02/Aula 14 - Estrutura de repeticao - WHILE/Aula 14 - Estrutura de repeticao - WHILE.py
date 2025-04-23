#ESTRUTURA DE REPETIÇÃO WHILE (enquanto)
import os
os.system('cls||clear')

for c in range (1,10):
    print(c)
print('Fim')

c = 1
while c < 10:
    print(c)
    c+=1
print('FIM')



for c in range(1,3):
    n = int(input('Digite um valor: '))
print('FIM')

n = 1
while n!=0:
    n = int(input('Digite um numero: '))
print('FIM')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = input('Deseja continuar? (S/N)').upper() #coloca em maiuscula
print('== FIM ==')


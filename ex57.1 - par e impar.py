# Digite os numeros e diga quantos são pares e quantos são ímpares.
import os
os.system('cls||clear')

c = 1
par = impar = 0
while c!=0:
    c = int(input('Digite um numero: '))
    if c!=0:    
        if c % 2 == 0:
            par+=1    
        else:
            impar+=1

print('== FIM ==')
print(f'São {impar} numero(s) impar(es) e {par} numero(s) par(es)')
     
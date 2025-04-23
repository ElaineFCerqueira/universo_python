# cont = 1

# while cont <=10:
#     print(cont)
#     cont += 1
# print('Acabou!!!!')

cont = soma = 0

while True:
    n = int(input('Digite um numero: '))
    cont+=1
    
    
    if n == 999:
        break
    soma+=n
print(f'A soma vale {soma}')



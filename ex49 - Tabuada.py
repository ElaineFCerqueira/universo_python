#Refaça o DESAFIO 9, mostrando a tabuada de um número que o 
# usuário escolher, só que agora utilizando um laço for.


num = int(input('Digite um numero: '))
for c in range(0,11):
    mult = c*num
    print(f'{c} x {num} = {mult}')
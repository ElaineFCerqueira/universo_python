import os
os.system('cls||clear')

'''
#AS TUPLAS SÃO IMUTÁVEIS
TUPLAS >>>    ()
LISTAS >>>    []
DICIONARIOS > {}
'''

# lanche = ('Hamburger', 'Suco', 'Pizza','Pudim','Batata frita')

# print(lanche[0])

# #Quantos elementos tem a tupla
# print(len(lanche))

# #Acessando o ultimo elemento
# print((lanche[-1]))

# print('>'*40)

# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Comi pra caramba!')

# print('>'*40)

# for cont in range (0,len(lanche)):
#     print(f'Preciso de: {lanche[cont]}. Na posição: {cont}')

# print('>'*40)

# for pos,comida in enumerate(lanche):
#     print(f'Preciso de: {comida}. Na posição: {pos}')
    
# print('>'*40)

# print(sorted(lanche)) #coloca o lanche em ordem

print('>'*40)

a = (2,5,6)
b = (9,6,3)
c = b + a
print(c)

print(c.count(3)) #conta quantas vezes aparece o elemento na lista

print(c.index(3)) #conta em que posição está o elemento 

del(c) #deleta a tupla
print(c)
'''
Se usarmos a estrutura for c in range(0, 10, 3): 
no Python e colocarmos dentro do bloco um comando print(c), 
quais serão os valores impressos na tela do terminal?
'''
for c in range(0,10,3):
    print(c)
    
'''
Se usarmos a estrutura for c in range(0, 5): 
no Python e colocarmos dentro do bloco um comando print(c), 
quais serão os valores impressos na tela do terminal?
'''
for c in range(0,5):
    print(c, end='')
    
    
'''
Que comando podemos usar para gerar um número inteiro aleatório, entre 10 e 100?
'''
from random import randint

n = randint(10,101)
print(n)
'''
Listas podem ser modificadas

'''

lanche = ['pizza', 'suco']
lanche.append('picole') #adicionar na lista
print(lanche)

lanche.insert(0,'cachorro-quente') #adiciona o elemento em uma determinada posição
print(lanche)

del lanche[3] #deleta o elemento da posição indicada
print(lanche)

lanche.pop() #deleta o ultimo item
print(lanche)

lanche.remove('pizza') #deleta o elemento pelo nome
print(lanche)

if 'pizza' in lanche:
    lanche.remove('pizza')
else:
    print('Não existe na lista')


valores = list(range(4,11))
print(valores)

num = [3,8,4,1,9,2,5,7]
num.sort()
print(num)

num.sort(reverse=True)
print(num)

num[2] = 20
print(num)

num.append(60)
print(num)

len(num)
print(f'Essa lista tem {len(num)} elementos')


numeros = []
numeros.append(5)
numeros.append(9)
numeros.append(16)

for c, v in enumerate(numeros):
    print(f'Na posição {c} encontrei o valor: {v}')

lote = []

for contador in range(0,5):
    lote.append(int(input('Digite um numero: ')))
print(lote)
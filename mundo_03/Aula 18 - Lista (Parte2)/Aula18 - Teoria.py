import os
os.system('cls||clear')

#LISTAS DENTRO DAS LISTAS:


# # dados = list()

# # dados.append('Pedro')
# # dados.append(25)


# # print(dados[0])
# # print(dados[1])

# pessoas = []
# pessoas.append(dados[:])
# print(pessoas)
# print(pessoas[0][0])



# teste = []
# teste.append('Elaine')
# teste.append(30)

# #print(teste)

# galera = []
# galera.append(teste[:])
# teste [0] = 'Ju'
# teste [1] = 32
# galera.append(teste[:])
# print(galera)


# galera = [['Jeane',20],['Jai',15],['Juci',10],['Ju',10]]
# #print(galera[0])
# for pessoa in galera:
#     print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')


galera = []
dados = []
total_maior = total_menor = 0

for contador in range(0,3):
    dados.append(input('Digite um nome: '))
    dados.append(int(input('Digite a idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)

for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'São maiores de idade: {pessoa[0]}')
        total_maior+=1
    else:
        print(f'São menores de idade: {pessoa[0]}')
        total_menor+=1
print(f'temos {total_maior} pessoas maiores de idade e {total_menor} menores de idade')

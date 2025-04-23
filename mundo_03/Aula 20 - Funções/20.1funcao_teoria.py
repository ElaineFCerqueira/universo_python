import os
os.system('cls||clear')

# def mostar_linha():
#     print('-'*40)
#     print('-'*40)

# mostar_linha()
# print('SISTEMA DE ALUNOS')
# mostar_linha()
# print('CADASTRO DE FUNCIONÁRIOS')
# mostar_linha()
# print('ERRO DO SISTEMA')

#///////////////////////////////////////////////////////////////////////////////////

# def lin():
#     print('-' *30)

# #programa principal
# lin()
# print('Curso em video')
# lin()
# print('Aprenda PYTHON')
# lin()
# print('Gustavo Guanabara')
# lin()


#///////////////////////////////////////////////////////////////////////////////////

# def mensagem(msg):
#     print('-'*30)
#     print(msg)
#     print('-'*30)


# mensagem('Sistema de alunos')

#///////////////////////////////////////////////////////////////////////////////////

# def titulo(txt):
#     print('-'*30)
#     print(txt)
#     print('-'*30)

# #programa principal
# titulo(' Curso em video ')
# titulo(' Aprenda PYTHON ')
# titulo(' Gustavo Guanabara ')

#///////////////////////////////////////////////////////////////////////////////////

# def soma(a,b):
#     s = a + b
#     print(s)


# #programa principal
# soma(4,5)
# soma(8,9)
# soma(2,1)

#///////////////////////////////////////////////////////////////////////////////////

# def soma(a,b):
#     print(f' A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma de A + B = {s}')


# #programa principal
# soma(a = 4,b = 5)
# soma(3,9)

#///////////////////////////////////////////////////////////////////////////////////

#ENPACOTANDO PARAMETROS
# def contador (*num):
    
#     for valor in num:
#         print(valor, end=' ')
    

# contador(5,7,3,14)
# contador(8,4,7)
# contador(14,9,7,1,0,6)

#////////////////////////////////////////////////////////////////////////////////////

# def dobra(lista):
#     pos = 0
#     while pos < len(lista):
#         lista[pos]*=2
#         pos+=1


# valores = [7,2,3,6,5,9]
# dobra(valores)
# print(valores)

#////////////////////////////////////////////////////////////////////////////////////
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos {valores} temos {s}')


soma(2,5)
soma(2,9,4,8)
# def soma(a,b): # com parametro
#     s = a + b
#     print(f'A soma de {a} + {b} = {s}')


# #Programa Principal
# soma(4,5)
# soma(2,1)
# soma(8,9)


# def contador(*num): #desenpacotar os numeros
#     print(f'Os numeros são: {num}')
#     tam = len(num)
#     print(f'A lista tem {tam} elementos')
#     for valor in num:
#         print(valor)
#     print('FIM')

# #Programa principal
# contador(1,2,3,4,5)
# contador(5,9,8,7)
# contador(2,5,6)
# contador(1,5)


# def dobra(lista):
#     pos=0
#     while pos<len(lista):
#         lista[pos]*=2
#         pos+=1
#     print(lista)


# #programa Principal
# valores = [7,2,5,0,4]
# dobra(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} é igual a {s}')


soma(5,2)
soma(4,7,9)
soma(1,6,3,8)
##### AJUDA INTERATIVA

#help(print)

#print(input.__doc__)

###### DOCSSTRINGSs

# def contador(i,f,p):
#     '''
#     -> Faz uma contagem e mostra na tela.
#     : para i: inicio da contagem
#     : para f: final da contagem
#     : para p: passo da contagem
#     : return: sem retorno
#     Função criada por Elaine com ajuda com o Canal Curso em Video
#     '''
#     for cont in range(i,f,p):
#         print(cont, end=' ')
#     print('FIM')

# help(contador)


###### PARAMETROS OPCIONAIS

def soma(a=0,b=0,c=0): #parametros opcionais
    '''
        -> Faz uma soma dos valores e mostra na tela.
    : para a: primeiro valor
    : para b: segundo valor
    : para c: terceiro valor 
    : return: sem retorno
    Função criada por Elaine com ajuda com o Canal Curso em Video
    '''
    s = a + b + c
    print(f'A soma dos valores é {s}')


soma(2,5,3)
soma(2,5)
soma(9)

help(soma)

### ESCOPO DE DECLARAÇÕES(VARIAVÉIS)

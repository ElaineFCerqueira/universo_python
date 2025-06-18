'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e 
mostre uma mensagem com tamanho adaptável.                      
Ex:                                                                                                                                                                        escreva(‘Olá, Mundo!’) Saída:                                                                                                                          
~~~~~~~~~                                                                                                                  
Olá, Mundo!                                                                  
~~~~~~~~~                        

'''

def escreva(msg):
    print('~'*len(msg))
    print(msg)
    print('~'*len(msg))

#Programa Principal
escreva('Olá mundo!')
escreva('Bahia é o mundo')
escreva('Você não é todo mundo')
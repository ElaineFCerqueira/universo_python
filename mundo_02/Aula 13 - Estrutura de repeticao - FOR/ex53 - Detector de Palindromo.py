import os
os.system('cls||clear')

def logo_senai():
    print('=== SENAI ===')

def palindromo(frase):
    palavras = frase.split() # separa por palavras
    junto = ''.join(palavras) #junta desconsiderando espaços
    inverso = junto[::-1]
    #for letra in range(len(junto) -1,-1,-1):
    #    inverso += junto[letra]
    print(f'O inverso de {junto} é {inverso}')
    if inverso == junto:
        print('Temos um palíndro!')
    else:
        print('Não é um palíndromo')







frase = input('Digite uma frase: ') .strip() .upper() # strip= tira os espaços // upper= colocar me maiscula


logo_senai()
palindromo(frase)

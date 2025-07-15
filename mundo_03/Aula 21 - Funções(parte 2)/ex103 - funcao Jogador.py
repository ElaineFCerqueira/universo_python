def ficha(jog='desconhecido',gols=0):
    print(f'O jogador {jog} fez {gols} gol(s) no campeonato')


#programa principal
nome = input('Nome do jogador: ')
gol = input('Numero de gols: ')
if gol.isnumeric():
    gol = int(gol)
else:
    gol=0

if nome.strip() == '':
    ficha(gols = gol)
else:
    ficha(nome,gol)
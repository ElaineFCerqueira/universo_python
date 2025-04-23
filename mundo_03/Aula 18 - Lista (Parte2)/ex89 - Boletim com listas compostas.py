lista = []


while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media=(nota1+nota2)/2
    lista.append([nome,[nota1,nota2],media])

    

    resposta = input('Deseja continuar? (S/N): ').strip() .upper()[0]
    if resposta in 'Nn':
        break
print('-='*30)
for i , l in lista:
    print(f'{i} - {l} = média {media}')
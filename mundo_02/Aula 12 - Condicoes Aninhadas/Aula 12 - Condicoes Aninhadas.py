# if (se)
#elif (senão se)
#else (senão)

nome = input('Qual o seu nome? ')

if nome == 'Nane':
    print(f'Que nome lindo!{nome}')
elif nome == 'Maria' or nome == 'João' or nome =='Pedro':
    print('Seu nome é muito comum no Brasil')
elif nome in ('Ana Cláudia Jessica Juliana'):
    print(f'{nome} é um belo nome feminino')
else:
    print(f'Seu nome é bem normal,{nome}')
print('Tenha um bom dia!')
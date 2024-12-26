
import os
os.system('cls||clear')


QuantPessoas = int(input('Quantos usuários serão cadastrados? '))
lista = []
PessoaCadastrada = []

def buscar(pessoa):
  nome_procurado = input("Digitar o nome da pessoa que deseja buscar: ")
  for item in enumerate(lista):
    if pessoa == nome_procurado:
      print(f'{item} - {PessoaCadastrada}')
    else:
      print('Usuário não localizado')




while True:
    print('''Menu de Opções: 
          1 - Cadastrar novo usuário
          2 - Listar todos os usuários cadastrados
          3 – Buscar usuário pelo nome
          4 - Sair do sistema
          ''')
    opcoes = int(input('Digite a opção desejada: '))

    match (opcoes):
            case 1:
              if QuantPessoas > len(lista):
                pessoa = input('Adicione o nome do usuário: ')
                idade = int(input('Digite a idade do usuário: '))
                
                PessoaCadastrada = (f'Nome: {pessoa}, Idade: {idade}')
                lista.append(PessoaCadastrada)
                           
                print(f"Atributos Nome: {pessoa} ; Idade: {idade} ,foram cadastrados com sucesso")

            case 2:
              for i, PessoaCadastrada in enumerate(lista, start=1): #enumerate conta a quantidade de loops
                    print(f'{i}º - {PessoaCadastrada}')

            case 3:
              buscar(pessoa)
              
                        
             
            case 4:
              print('O programa foi finalizado')
              break


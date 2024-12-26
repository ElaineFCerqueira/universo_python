
import os
os.system('cls||clear')


QuantPessoas = int(input('Quantos usuários serão cadastrados? '))
pessoas = [""]*QuantPessoas 
idades =[0] *QuantPessoas
PessoaCadastrada = 0


while True:
    print('''Menu de Opções: 
          1 - Cadastrar novo usuário
          2 - Listar todos os usuários cadastrados
          3 - Sair do sistema
          ''')
    opcoes = int(input('Digite a opção desejada: '))

    match (opcoes):
            case 1:
              if PessoaCadastrada < QuantPessoas:
                pessoa = input('Adicione o nome do usuário: ')
                idade = int(input('Digite a idade do usuário: '))
                
                pessoas[PessoaCadastrada] = pessoa
                idades[PessoaCadastrada] = idade
                
                PessoaCadastrada +=1
                print(f" Nome: {pessoa} ; Idade: {idade},foram cadastrados com sucesso")

            case 2:
              for i in range(PessoaCadastrada):
                   print(f" Nome: {pessoas[i]}, Idade: {idades[i]}")

            case 3:
              print('O programa foi finalizado')
              break



# Definir uma lista vazia para armazenar os usuários cadastrados

usuarios = []


# Função para cadastrar um novo usuário

def cadastrar_usuario():
   nome = input("Digite o nome do usuário: ")
   idade = int(input("Digite a idade do usuário: "))
   usuarios.append({"nome": nome, "idade": idade})
   print("Usuário cadastrado com sucesso!")


# Função para listar todos os usuários cadastrados

def listar_usuarios():
   if not usuarios:
       print("Nenhum usuário cadastrado.")
   else:
       print("Usuários cadastrados:")
       for usuario in usuarios:
           print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}")


# Loop principal do programa

while True:

   print("\nMenu:")

   print("1 – Cadastrar novo usuário")

   print("2 – Listar todos os usuários cadastrados")

   print("3 – Sair do sistema")

   

   escolha = input("Escolha uma opção: ")

   

   if escolha == '1':

       cadastrar_usuario()

   elif escolha == '2':

       listar_usuarios()

   elif escolha == '3':

       print("Saindo do sistema. Até mais!")

       break

   else:

       print("Opção inválida. Tente novamente.")
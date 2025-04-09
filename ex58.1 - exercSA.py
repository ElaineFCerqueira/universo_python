# Lista para armazenar os usuários cadastrados
usuarios = []

# Estrutura de repetição que continuará até o usuário escolher a opção de sair (3)
while True:
    # Exibir o menu de opções
    print("\nMenu de Opções:")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar todos os usuários cadastrados")
    print("3 - Sair do sistema")

    # Solicitar a opção do usuário
    opcao = int(input("Digite a opção desejada: "))

    # Opção para cadastrar novo usuário
    if opcao == 1:
        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        usuarios.append({"nome": nome, "idade": idade})
        print("Usuário cadastrado com sucesso!")

    # Opção para listar todos os usuários cadastrados
    elif opcao == 2:
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.")
        else:
            print("Usuários cadastrados:")
            for usuario in usuarios:
                print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}")

    # Opção para sair do sistema
    elif opcao == 3:
        print("Saindo do sistema...")
        break

    # Caso o usuário digite uma opção inválida
    else:
        print("Opção inválida. Tente novamente.")

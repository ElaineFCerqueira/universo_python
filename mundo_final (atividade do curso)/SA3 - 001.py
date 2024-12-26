
quant_usuario = int(input('Quantos usuários deseja cadastrar? '))
usuarios = []

while quant_usuario > 0:
        
    print("\nMenu de Opções:")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar todos os usuários cadastrados")
    print("3 - Sair do sistema")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        quant_usuario-=1
        if quant_usuario == usuarios:
            print('A lista está cheia')
        else:
            nome = input("Digite o nome do usuário: ")
            idade = int(input("Digite a idade do usuário: "))
            usuarios.append({"nome": nome, "idade": idade})
            print("Usuário cadastrado com sucesso!")

    
    elif opcao == 2:
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.")
        else:
            print("Usuários cadastrados:")
            for usuario in usuarios:
                print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}")

   
    elif opcao == 3:
        print("Saindo do sistema...")
        break

   

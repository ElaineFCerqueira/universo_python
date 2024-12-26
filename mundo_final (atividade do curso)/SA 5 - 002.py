max_size = 25  # Tamanho máximo da fila
fila = [""] * max_size  # Fila inicializada com strings vazias
inicio = 0  # Índice do início da fila
fim = -1  # Índice do fim da fila
tamanho = 0  # Número de elementos na fila

 



def vazia():
    if tamanho == 0:
        return True
    else:
      return False



def cheia():
    return tamanho == max_size

 

# Função para adicionar um elemento no fim da fila (enfileirar)

def adicionar(livro):
    global fim, tamanho
    if not cheia():  # Verifica se a fila não está cheia
        fim = (fim + 1) % max_size  # Incrementa o índice circularmente
        fila[fim] = nome
        tamanho += 1
        print(f"{nome} foi enfileirado com sucesso.")

    else:
        print("Erro: A fila está cheia!")

 

# Função para remover e retornar o elemento no início da fila (desenfileirar)

def desenfileirar():

    global inicio, tamanho

    if not vazia():

        nome = fila[inicio]

        fila[inicio] = ""  # Remove o valor do início

        inicio = (inicio + 1) % max_size  # Incrementa o índice circularmente

        tamanho -= 1

        print(f"{nome} foi desenfileirado.")

        return nome

    else:

        print("Erro: A fila está vazia!")

        return None

 

# Função para limpar a fila (remover todos os elementos)

def limpar():

    global inicio, fim, tamanho

    while not vazia():

        desenfileirar()

    print("Fila foi completamente esvaziada.")

 

# Função para listar todos os elementos da fila

def listar():

    if not vazia():

        print("Elementos na fila (do início para o fim):")

        i = inicio

        for _ in range(tamanho):

            print(fila[i])

            i = (i + 1) % max_size

    else:

        print("A fila está vazia.")

 

# Menu para o usuário enfileirar valores

while True:

    print('''\nEscolha uma opção:
        1 - Adicionar um livro
        2 - Desenfileirar
        3 - Listar os elementos da fila
        4 - Limpar a fila
        5 - Sair''')
  

    opcao = input("Digite sua opção: ")

 

    if opcao == '1':

        nome = input("Digite o nome para enfileirar: ")

        enfileirar(nome)

    elif opcao == '2':

        desenfileirar()

    elif opcao == '3':

        listar()

    elif opcao == '4':

        limpar()

    elif opcao == '5':

        print("Saindo do programa.")

        break

    else:

        print("Opção inválida! Tente novamente.")
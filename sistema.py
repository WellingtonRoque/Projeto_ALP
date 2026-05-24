# ==========================================
# SISTEMA DE GESTÃO COMERCIAL
# ==========================================

# ---------- MENU ----------

def menu_principal():

    print("\n===================================")
    print("      SISTEMA COMERCIAL")
    print("===================================")

    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Buscar Produto")
    print("4 - Remover Produto")
    print("5 - Cadastrar Cliente")
    print("6 - Listar Clientes")
    print("0 - Sair")


# ---------- PRODUTOS ----------

def cadastrar_produto():

    try:

        produto = input("Digite o nome do produto: ")

        preco = float(input("Digite o preço do produto: "))

        arquivo = open("produtos.txt", "a", encoding="utf-8")

        arquivo.write(f"{produto} - R$ {preco:.2f}\n")

        arquivo.close()

        print("\n✅ Produto cadastrado com sucesso")

    except ValueError:

        print("\n❌ Preço inválido")


def listar_produtos():

    try:

        arquivo = open("produtos.txt", "r", encoding="utf-8")

        produtos = arquivo.readlines()

        arquivo.close()

        print("\n===== LISTA DE PRODUTOS =====")

        if len(produtos) == 0:

            print("Nenhum produto cadastrado")

        else:

            for produto in produtos:

                print(produto)

    except FileNotFoundError:

        print("\n❌ Arquivo de produtos não encontrado")


def buscar_produto():

    busca = input("Digite o nome do produto: ")

    try:

        arquivo = open("produtos.txt", "r", encoding="utf-8")

        produtos = arquivo.readlines()

        arquivo.close()

        encontrado = False

        for produto in produtos:

            if busca.lower() in produto.lower():

                print("\n✅ Produto encontrado:")
                print(produto)

                encontrado = True

        if not encontrado:

            print("\n❌ Produto não encontrado")

    except FileNotFoundError:

        print("\n❌ Arquivo de produtos não encontrado")


def remover_produto():

    nome = input("Digite o produto para remover: ")

    try:

        arquivo = open("produtos.txt", "r", encoding="utf-8")

        produtos = arquivo.readlines()

        arquivo.close()

        arquivo = open("produtos.txt", "w", encoding="utf-8")

        removido = False

        for produto in produtos:

            if nome.lower() not in produto.lower():

                arquivo.write(produto)

            else:

                removido = True

        arquivo.close()

        if removido:

            print("\n✅ Produto removido com sucesso")

        else:

            print("\n❌ Produto não encontrado")

    except FileNotFoundError:

        print("\n❌ Arquivo de produtos não encontrado")


# ---------- CLIENTES ----------

def cadastrar_cliente():

    cliente = input("Digite o nome do cliente: ")

    arquivo = open("clientes.txt", "a", encoding="utf-8")

    arquivo.write(cliente + "\n")

    arquivo.close()

    print("\n✅ Cliente cadastrado com sucesso")


def listar_clientes():

    try:

        arquivo = open("clientes.txt", "r", encoding="utf-8")

        clientes = arquivo.readlines()

        arquivo.close()

        print("\n===== LISTA DE CLIENTES =====")

        if len(clientes) == 0:

            print("Nenhum cliente cadastrado")

        else:

            for cliente in clientes:

                print(cliente)

    except FileNotFoundError:

        print("\n❌ Arquivo de clientes não encontrado")


# ---------- SISTEMA PRINCIPAL ----------

opcao = ""

while opcao != "0":

    menu_principal()

    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":

        cadastrar_produto()

    elif opcao == "2":

        listar_produtos()

    elif opcao == "3":

        buscar_produto()

    elif opcao == "4":

        remover_produto()

    elif opcao == "5":

        cadastrar_cliente()

    elif opcao == "6":

        listar_clientes()

    elif opcao == "0":

        print("\n🚀 Sistema encerrado")

    else:

        print("\n❌ Opção inválida")
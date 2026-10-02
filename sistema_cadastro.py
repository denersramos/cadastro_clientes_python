#Função para cadastrar cliente

def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    cpf = input("CPF: ")
    data_nascimento = input("Data de nascimento: ")
    endereco = input("Endereço: ")
    celular = input("Número de celular: ")
    email = input("E-mail: ")

    return nome, cpf, data_nascimento, endereco, celular, email

#Começo do programa

while True:

    print("\n" "O que você deseja fazer?")
    print("\n" "1. Cadastrar cliente.")
    print("2. Consultar cliente.")
    print("3. Alterar dados de um cliente existente.")
    print("4. Excluir cliente.")
    print("5. Listar todos os clientes cadastrados.")
    print("6. Sair do programa.")

    opcao = input("\n" "Escolha uma opção: ")

    #Cadastrar cliente

    if opcao == "1":
        print("\n" f"{cadastrar_cliente()}")
        print("\n" "Cliente cadastrado com sucesso!")
        continue

    #Consultar cliente

    elif opcao == "2":
        print("\n" "Digite o CPF do cliente que deseja consultar: ")

    #Alterar dados de um cliente existente

    elif opcao == "3":
        print("\n" "Digite o CPF do cliente que deseja alterar os dados: ")

    #Excluir cliente

    elif opcao == "4":
        print("\n" "Digite o CPF do cliente que deseja excluir: ")

    #Listar todos os clientes cadastrados

    elif opcao == "5":
        print("\n" "Listando todos os clientes cadastrados: ")

    #Sair do programa
    
    elif opcao == "6":
        print("\n" "Saindo do programa...")
        break

    #Se a opção escolhida for inválida
    else:
        print("\n" "Opção inválida. Por favor, escolha uma opção válida.")
        continue

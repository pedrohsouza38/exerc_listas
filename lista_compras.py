# Inicializa a lista vazia que irá armazenar os produtos
lista_compras = []

# Estrutura de repetição que mantém o menu ativo até o usuário escolher sair
while True:
    # Exibe o menu de opções
    print("\n--- MENU ---")
    print("1 - Adicionar a lista")
    print("2 - Pesquisar item")
    print("3 - Remover item")
    print("4 - Alterar item")
    print("5 - Listar produtos")
    print("6 - Sair")
    
    # Solicita a escolha do usuário
    opcao = input("\nEscolha uma opção (1-6): ")
    
    # OPÇÃO 1: Adicionar produtos
    if opcao == '1':
        print("\n--- ADICIONAR PRODUTOS ---")
        print("Digite os produtos. Digite 'sair' para voltar ao menu.")
        while True:
            item = input("Produto: ").lower() # Transforma a entrada em letras minúsculas
            if item == 'sair':
                break
            lista_compras.append(item) # Adiciona o item na lista
            print(f"'{item}' adicionado!")
            
    # OPÇÃO 2: Pesquisar item
    elif opcao == '2':
        print("\n--- PESQUISAR ITEM ---")
        item_pesquisa = input("Digite o produto que deseja buscar: ").lower()
        if item_pesquisa in lista_compras:
            print("Produto encontrado na lista!")
        else:
            print("Produto não encontrado.")
            
    # OPÇÃO 3: Remover item
    elif opcao == '3':
        print("\n--- REMOVER ITEM ---")
        item_remocao = input("Digite o produto que deseja remover: ").lower()
        if item_remocao in lista_compras:
            lista_compras.remove(item_remocao) # Remove o item da lista
            print("Produto encontrado e removido com sucesso!")
        else:
            print("Produto não encontrado.")
            
    # OPÇÃO 4: Alterar item
    elif opcao == '4':
        print("\n--- ALTERAR ITEM ---")
        item_antigo = input("Digite o nome do produto que deseja alterar: ").lower()
        if item_antigo in lista_compras:
            item_novo = input("Digite o NOVO nome do produto: ").lower()
            # Encontra a posição do item antigo e substitui pelo novo
            posicao = lista_compras.index(item_antigo)
            lista_compras[posicao] = item_novo
            print("Produto alterado com sucesso!")
        else:
            print("Produto não encontrado.")
            
    # OPÇÃO 5: Listar produtos
    elif opcao == '5':
        print("\n--- LISTA DE COMPRAS ---")
        if len(lista_compras) == 0:
            print("Lista vazia")
        else:
            # Exibe cada produto da lista
            for produto in lista_compras:
                print(f"- {produto}")
                
    # OPÇÃO 6: Sair do programa
    elif opcao == '6':
        print("\nPrograma encerrado com sucesso!")
        break # Encerra o loop principal
        
    # Tratamento para opções inválidas
    else:
        print("\nOpção inválida! Por favor, escolha um número de 1 a 6.")
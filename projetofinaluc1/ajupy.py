print ('#' * 20, 'BEM VINDO A NARA HORTI FRUTI', '#'*20)
produtos = []
while True:
    print("1 - Adicionar item")
    print("2 - Listar itens")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1: 
        escolha_produto = input('Digite o produto que deseja: ').title()
        produtos.append(escolha_produto)

    elif opcao == 2:
        if len(produtos) == 0:
            print("Nenhum produto cadastrado!")
        else:
            for i in produtos:
                print(f'Produto {i}')

    elif opcao == 3:
        break

    else:
        print('Escolha uma opção válida')
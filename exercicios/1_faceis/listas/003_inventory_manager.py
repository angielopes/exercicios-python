"""Crie um programa que gerencie o estoque de uma loja. O programa deve permitir:
1. Adicionar produtos ao estoque com:
    - Nome do produto.
    - Quantidade inicial do produto.
2. Remover produtos do estoque:
    - O usuário deve informar o nome do produto e a quantidade a ser retirada.
    - Caso a quantidade retirada seja maior do que a disponível, exiba uma mensagem de erro
    e peça outra entrada.
3. Exibir o estoque atualizado:
    - Após cada operação de adição ou remoção, mostre a lista de produtos e suas quantidades.
*  Desafio bônus:
    - Não permita que produtos com o mesmo nome sejam adicionados ao estoque.
    Se isso ocorrer, apenas atualize a quantidade.
"""

estoque = []

while True:
    # Menu do estoque
    print(
        """\nOPÇÕES:
    [1] Adicionar produto
    [2] Remover produto
    [3] Ver estoque
    [4] Sair
    """
    )
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    # Sair do programa
    if opcao == 4:
        print("Programa finalizado...")
        break

    # Adicionar produtos
    elif opcao == 1:
        produto = input("Nome do produto: ").capitalize()
        qtd_inicial = int(input("Quantidade a ser adicionada: "))

        # Verificar se o produto já existe no estoque
        for item in estoque:
            if item[0] == produto:
                item[1] += qtd_inicial
                print(f"{qtd_inicial} unidades adicionados ao produto {produto}")
                break
        else:
            estoque.append([produto, qtd_inicial])
            print(f"{qtd_inicial} unidades adicionadas ao novo produto {produto}")

    # Remover produtos
    elif opcao == 2:
        remover_produto = input("Nome do produto: ").capitalize()
        qtd_retirada = int(input("Quantidade a ser retirada: "))

        for item in estoque:
            if item[0] == remover_produto:
                if item[1] >= qtd_retirada:  # Verifica se tem quantidade suficiente
                    item[1] -= qtd_retirada
                    print(f"{qtd_retirada} removidos do produto {remover_produto}")
                    if item[1] == 0:
                        estoque.remove(item)
                        print(
                            f"Produto {remover_produto} esgotado e removido do estoque."
                        )
                else:
                    print("Quantidade insuficiente em estoque!")
                break
        else:
            print("Produto não encontrado.")

    # Mostrar estoque
    elif opcao == 3:
        print("\nExibindo estoque completo...")
    else:
        print("Opção inválida. Tente novamente.")

    # Exibir estoque após cada iteração
    if estoque:
        print("\nEstoque atual:")
        for item in estoque:
            print(f"{item[0]}: {item[1]} unidades")
    else:
        print("Estoque está vazio.")

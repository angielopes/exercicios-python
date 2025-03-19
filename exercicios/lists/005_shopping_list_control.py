"""Crie um programa para gerenciar uma lista de compras.
Cada item terá um nome do produto, sua quantidade e o preço unitário. O programa deverá permitir:
1. Adicionar um produto à lista de compras.
2. Remover um produto da lista.
3. Calcular o valor total da compra.
4. Exibir todos os itens com nome, quantidade e preço total de cada produto."""

lista_compra = []

while True:
    print(
        """
            Opções:
    [1] Adicionar produto
    [2] Remover produto
    [3] Ver lista de compras
    [4] Calcular total
    [5] Sair"""
    )

    try:
        opcao = int(input("\nEscolha a opção: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    # Sair do programa
    if opcao == 5:
        print("Programa encerrado...")
        break

    # Adicionar produtos, quantidade e valor
    elif opcao == 1:
        produto = input("Nome do produto: ").capitalize().strip()
        try:
            qtd_produto = int(input("Quantidade: "))
            preco_unitario = float(input("Preço unitário: "))
        except ValueError:
            print("Quantidade e preço preciam ser números válidos.")
            continue

        # Verificar se o item já existe (se existir, irá apenas adicionar quantidade)
        for item in lista_compra:
            if item[0] == produto:
                item[1] += qtd_produto
                print(
                    f"{qtd_produto} unidades adicionadas ao produto {produto} na lista de compra."
                )
                break
        else:
            lista_compra.append([produto, qtd_produto, preco_unitario])

    # Remover produtos
    elif opcao == 2:
        remover_produto = (
            input("Qual produto deseja remover da lista? ").capitalize().strip()
        )
        for item in lista_compra:
            if item[0] == remover_produto:
                lista_compra.remove(item)
                print(f"{remover_produto} removido da lista.")
                break
        else:
            print(f"O produto {remover_produto} não está na lista de compra.")

    # Visualizar lista de compra
    elif opcao == 3:
        if lista_compra:
            print("\nLISTA DE COMPRA:")
            for item in lista_compra:
                valor_total_produto = item[1] * item[2]
                print(
                    f"{item[0]} - Quantidade: {item[1]} - Preço Unitário: R$ {item[2]:.2f} - Total: R$ {valor_total_produto:.2f}"
                )
        else:
            print("Lista de compras está vázia.")

    # Calcular valor total da compra
    elif opcao == 4:
        if lista_compra:
            valor_total_compra = sum(item[1] * item[2] for item in lista_compra)
            print(f"\nValor total da compra: R$ {valor_total_compra}")
        else:
            print("Lista de compras está vázia.")

    else:
        print("Opção inválida. Tente novamente.")

"""É mesma coisa que
    valor_total_compra = 0
    for item in lista_compras:
        valor_total_compras += item[1] * item[2]"""

"""Crie um programa em Python para gerenciar o estoque de uma loja.
O programa deve oferecer as seguintes opções para o usuário:
1. Adicionar item ao estoque [OK]
    - O usuário deve informar o nome do item, a quantidade e o preço por unidade.
    O programa deve adicionar essas informações ao estoque.
2. Listar todos os itens do estoque [OK]
    - Mostre todos os itens registrados, exibindo o número do item, nome, quantidade
    e preço.
3. Atualizar a quantidade de um item
    - Permita que o usuário escolha o item pelo número e informe uma nova quantidade
    para o produto.
4. Remover itens com quantidade zero
    - Remova todos os itens cuja quantidade no estoque seja igual a zero.
5. Reordenar itens do estoque
    - Permita que o usuário escolha um item e mova-o para uma nova posição na lista.
6. Sair"""

estoque = []

while True:
    print(
        """
OPÇÕES:
[1] Adicionar item ao estoque
[2] Listar todos os itens do estoque
[3] Atualizar a quantidade de um item
[4] Remover itens com quantidade zero
[5] Reordenar itens do estoque
[6] Sair"""
    )

    # Validar se a opcão está correta
    try:
        opcao = int(input("Escolha a opção: "))
    except ValueError:
        print("Digite um número válido.")

    # Encerrar o programa
    if opcao == 6:
        print("Programa finalizado...")
        break

    # Adicionar item, quantidade e preço ao estoque
    elif opcao == 1:
        item = (
            input("Informe o nome do item a ser adicionado ao estoque: ")
            .capitalize()
            .strip()
        )
        # Verificar se o item já existe no estoque
        for itens in estoque:
            if itens[0] == item:
                print(
                    "Item já existe no estoque. Se quiser adicionar unidades ao item, volte ao menú e escolha a opção [3]"
                )
                break
        # Adicionando quantidade e preço, se o item não existir no estoque
        else:
            quantidade = int(input("Informe a quantidade: "))
            preco = float(input("Informe o preço da unidade: "))
            estoque.append([item, quantidade, preco])
            print(
                f"{quantidade} unidades do item '{item.upper()}' no valor de R$ {preco} foram adicionadas ao estoque."
            )

    # Listar itens do estoque
    elif opcao == 2:
        if estoque:
            print("\nESTOQUE:")
            for indice, (item, quantidade, preco) in enumerate(estoque, start=1):
                print(
                    f"{indice}. {item} - Quantidade: {quantidade} - Preço: R$ {preco}"
                )
        else:
            print("Estoque vázio.")

    # Adicionando unidades ao estoque
    elif opcao == 3:
        if estoque:
            while True:
                try: # Continuar
                    atualizar_qtd = int(
                input("Deseja adicionar ou retirar itens do estoque?\n"
                        "[1] Adicionar\n"
                        "[2] Retirar: "))
                

            # Produto
            while True:
                try:
                    indice_item = int(
                        input(
                            "Informe o número do item que deseja adicionar mais unidades ao estoque: "
                        )
                    )
                    if 1 <= indice_item <= len(estoque):
                        break
                    else:
                        print("Número fora do intervalo.")
                except ValueError:
                    print(
                        "Digite um número válido para selecionar o item ou a posição."
                    )

            # Retirar quantidade
            retirar_qtd = input("Deseja adicionar")

            # Adicionar quantidade
            while True:
                try:
                    adicionar_qtd = int(input("Informe a quantidade: "))
                    if adicionar_qtd > 0:
                        estoque[indice_item - 1][1] += adicionar_qtd
                        print(
                            f"Estoque do item '{estoque[indice_item -1][0].upper()}' atualizado com sucesso."
                        )
                        break
                    else:
                        print("Digite uma quantidade maior do que zero.")
                except ValueError:
                    print("Digite um número válido para a quantidade.")

        else:
            print("Estoque vázio.")

    # Remover itens que tem a quantidade nula
    elif opcao == 4:
        if estoque:
            qtd_nula = [itens for itens in estoque if itens[1] != 0]
            estoque = qtd_nula
            print("Itens sem estoque removidos!")
        else:
            print("Não existe nenhum item no estoque.")

    # Reordenar itens do estoque
    elif opcao == 5:
        if len(estoque) > 1:
            print("\nESTOQUE:")
            for indice, item in enumerate(estoque, start=1):
                print(f"{indice}. {item[0]}")

            while True:
                try:
                    posicao_atual = int(
                        input("Informe a posição do item que você deseja mover: ")
                    )
                    nova_posicao = int(input("Digite a posição de deseja colocá-lo: "))
                    if 1 <= posicao_atual <= len(estoque) and 1 <= nova_posicao <= len(
                        estoque
                    ):
                        item_movido = estoque.pop(posicao_atual - 1)
                        estoque.insert(nova_posicao - 1, item_movido)
                        print("Itens reordenados com sucesso!")
                        break
                    else:
                        print("Números informados fora do intervalo.")
                except ValueError:
                    print("Digite números válidos.")

        else:
            print("Estoque está vázio ou possui apenas um item.")

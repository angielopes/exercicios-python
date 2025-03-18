"""Você vai criar um programa que permita ao usuário gerenciar uma lista de livros lidos. O programa deve oferecer as seguintes opções:
1. Adicionar um livro à lista
- O usuário deve inserir o título e o autor do livro. A lista armazenará esses dados como uma sublista [título, autor].
2. Remover um livro da lista
- O programa deve mostrar os livros lidos com índices para que o usuário escolha qual remover.
3. Ordenar a lista
- Ofereça ao usuário a opção de ordenar os livros pelo título ou pelo autor, em ordem alfabética.
4. Pesquisar um livro
- Permita que o usuário digite um termo (palavra ou parte dela) e mostre todos os livros cujo título ou autor contenha esse termo.
5. Exibir a lista de livros lidos
- Mostre todos os livros armazenados, indicando o título e o autor.
6. Sair do programa."""

livros_lidos = []

while True:
    print(
        """
OPÇÕES:
[1] Adicionar um livro
[2] Remover um livro
[3] Ordenar a lista
[4] Pesquisar um livro
[5] Exibir todos os livros
[6] Sair"""
    )
    while True:
        try:
            opcao = int(input("Escolha a opção: "))
            if 1 <= opcao <= 6:
                break
            else:
                print("Escolha uma opção entre [1] e [6].")
        except ValueError:
            print("Escolha uma opção entre [1] e [6].")

    # Finalizar programa
    if opcao == 6:
        print("Programa de gerencimento de livros lidos finalizado. Até logo!")
        break

    # Adicionando livro e autor
    elif opcao == 1:
        while True:
            titulo = input("Título do livro: ").title().strip()
            if not titulo:
                print("O livro não pode estar vazio.")
                continue

            # Verificar se o livro já está na lista e adicioná-lo se não
            for livros in livros_lidos:
                if livros[0] == titulo:
                    print("Livro já está na lista. Adicione outro.")
                    break

            # Pedir autor e adioná-lo à lista juntamente com o título
            else:
                while True:
                    autor = input("Autor(a) do livro: ").title().strip()
                    if not autor:
                        print("O autor não pode estar vazio.")
                    else:
                        livros_lidos.append([titulo, autor])
                        print(f"Livro '{titulo}' adicionado com sucesso!")
                        break
            break

    # Remover livros pelo índice
    elif opcao == 2:
        if len(livros_lidos) != 0:
            print("\nLISTA DE LIVROS")
            for indice, (livro, autor) in enumerate(livros_lidos, start=1):
                print(f"{indice}. {livro} - Autor(a): {autor}")

            while True:
                try:
                    indice_livro = int(
                        input("Digite o índice do livro que deseja remover da lista: ")
                    )
                    if 1 <= indice_livro <= len(livros_lidos):
                        livro_removido = livros_lidos.pop(indice_livro - 1)
                        print(f"Livro '{livro_removido[0]}' removido com sucesso!")
                        break
                    else:
                        print("Índice não encontrado.")

                except ValueError:
                    print("Digite um índice válido.")
        else:
            print("A lista de livros está vázia.")

    # Ordenar a lista por título ou autor (ordem alfabética)
    elif opcao == 3:
        if livros_lidos:
            while True:
                try:
                    ordenar_livros = int(
                        input(
                            "Deseja ordenar por:\n"
                            "[1] Título\n"
                            "[2] Autor\n"
                            "Opção: "
                        )
                    )
                    # Ordenar pelo título
                    if ordenar_livros == 1:
                        livros_lidos.sort(key=lambda titulo: titulo[0])
                        print("Lista de livros ordenada pelo título!")
                        break
                    # Ordenar pelo autor
                    elif ordenar_livros == 2:
                        livros_lidos.sort(key=lambda autor: autor[1])
                        print("Lista de livros ordenada pelo autor!")
                        break
                    else:
                        print("Escolha [1] ou [2].")

                except ValueError:
                    print("Escolha [1] ou [2].")

        else:
            print("A lista de livros está vazia.")

    # Pesquisar o livro
    elif opcao == 4:
        if livros_lidos:
            while True:
                pesquisar_livro = input(
                    "Digite uma palavra chave para pesquisa: "
                ).strip()

                if not pesquisar_livro:
                    print("Campo não pode estar vazio.")
                    continue

                resultado = [  # Complexidade O(n) - Busca linear
                    f"{livro[0]} - Autor(a): {livro[1]}"
                    for livro in livros_lidos
                    if pesquisar_livro.lower() in livro[0].lower()
                    or pesquisar_livro in livro[1].lower()
                ]

                if resultado:
                    print("\nLivros encontrados:")
                    print("\n".join(resultado))
                    break
                else:
                    print(
                        "Nenhum livro encontrado com essa palavra chave. Tente novamente"
                    )

        else:
            print("A lista de livros está vazia.")

    # Listar os livros
    elif opcao == 5:
        if livros_lidos:
            for indice, (titulo, autor) in enumerate(livros_lidos, start=1):
                print(f"{indice}. {titulo} - Autor(a): {autor}")
        else:
            print("Lista de livros está vazia.")

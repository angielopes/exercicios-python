"""Crie um programa que permita ao usuário gerenciar uma lista de tarefas.
As opções incluem adicionar, remover, listar tarefas, mostrar tarefas incompletas e reordenar tarefas na lista.
1. Adicionar uma tarefa:
    - O usuário pode adicionar uma nova tarefa com um status inicial de "incompleta".
2. Listar todas as tarefas:
    - Exibir todas as tarefas da lista, numeradas, com seu status (incompleta ou completa).
3. Marcar uma tarefa como completa:
    - O usuário pode selecionar uma tarefa (pelo número) e marcá-la como "completa".
4. Remover tarefas completas:
    - Excluir da lista todas as tarefas marcadas como "completa".
5. Reordenar tarefas:
    - O usuário pode mover uma tarefa para uma nova posição na lista.
6. Sair."""

gerenciador_tarefas = []


while True:
    print(
        """
    OPÇÕES:
    [1] Adicionar tarefa
    [2] Listar tarefas
    [3] Marcar tarefa como completa
    [4] Remover tarefas completas
    [5] Reordenar tarefas
    [6] Sair"""
    )

    try:
        opcao = int(input("Escolha a opção: "))
    except ValueError:
        print(
            "Opção inválida. Tente novamente."
        )
        continue

    # Sair do programa
    if opcao == 6:
        print("Programa finalizado...")
        break

    # Adicionar tarefa
    elif opcao == 1:
        nova_tarefa = input(
            "Qual tarefa deseja adicionar? "
        ).strip()
        if nova_tarefa:
            gerenciador_tarefas.append(
                [nova_tarefa.capitalize(), "Incompleta"]
            )  # Adiciona a tarefa à lista com o status 'Incompleta'
            print(
                f"Tarefa '{nova_tarefa}' adicionada com sucesso!"
            )
        else:
            print("A tarefa não pode estar vazia.")

    # Listar as tarefas
    elif opcao == 2:
        if gerenciador_tarefas:
            print("\nTarefas registradas:")
            for indice, (nome, status) in enumerate(gerenciador_tarefas, start=1):
                print(f"{indice}. {nome} - {status}")
        else:
            print("Nenhuma tarefa registrada")

    # Marcar tarefa como 'completa'
    elif opcao == 3:
        if gerenciador_tarefas:
            try:
                numero_tarefa = int(
                    input("Digite o número da tarefa a ser marcada como concluída: ")
                )
                if (
                    0 <= numero_tarefa < len(gerenciador_tarefas)
                ):
                    gerenciador_tarefas[numero_tarefa - 1][
                        1
                    ] = "Completa"
                    print(
                        f"Tarefa '{gerenciador_tarefas[numero_tarefa - 1][0]}' marcada como completa!"
                    )
                else:
                    print("Número inválido.")
            except ValueError:
                print(
                    "Digite um número válido."
                )
        else:
            print("Nenhuma tarefa registrada.")

    # Remover tarefas completas
    elif opcao == 4:
        # Filtra as tarefas que não estão completas
        tarefas_incompletas = [
            tarefa
            for tarefa in gerenciador_tarefas
            if tarefa[1] != "Completa"  # [expressão for item in iterável if condição]
        ]
        if len(tarefas_incompletas) < len(
            gerenciador_tarefas
        ):  # Verifica se há tarefas completas
            gerenciador_tarefas = (
                tarefas_incompletas  # Atualiza a lista, removendo as tarefas completas
            )
            print(
                "Tarefas completas removidas!"
            )
        else:
            print(
                "Não existem tarefas completas na lista"
            )

    # Reordenar tarefas
    elif opcao == 5:
        if len(gerenciador_tarefas) > 1:
            try:
                numero_tarefa = int(
                    input("Digite o número da tarefa que deseja mover: ")
                )
                nova_posicao = int(
                    input("Digite a nova posição da tarefa: ")
                )

                # Verifica se o número da tarefa e a nova posição são válidos
                if 1 <= numero_tarefa <= len(
                    gerenciador_tarefas
                ) and 1 <= nova_posicao <= len(gerenciador_tarefas):
                    # Remove a tarefa da posição original e insere na nova posição
                    tarefa_movida = gerenciador_tarefas.pop(numero_tarefa - 1)
                    gerenciador_tarefas.insert(nova_posicao - 1, tarefa_movida)
                    print(
                        "Tarefa reordenada com sucesso!"
                    )
                else:
                    print(
                        "Número(s) fora do intervalo."
                    )
            except ValueError:
                print(
                    "Digite números válidos."
                )
        else:
            print(
                "Não há tarefas suficientes para reordenar."
            )

    # Opção do menu inválida
    else:
        print(
            "Opção inválida. Digite um número entre 1 e 6."
        )

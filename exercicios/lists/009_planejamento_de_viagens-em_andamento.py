"""Crie um sistema para planejar uma viagem em que o usuário possa organizar destinos, datas e orçamento estimado.
Utilize três listas paralelas para gerenciar as informações.
1. Adicionar Destino:
    - Permita ao usuário adicionar um novo destino, a data planejada e o orçamento estimado.
    - As informações devem ser armazenadas em listas paralelas:
        - destinos → lista de destinos.
        - datas → lista de datas planejadas.
        - orcamentos → lista de orçamentos.
2. Remover Destino:
    - Permita ao usuário remover um destino e as informações associadas (data e orçamento).
3. Atualizar Informações:
    - Permita alterar a data ou o orçamento de um destino existente.
4. Listar Viagens:
    - Exiba todos os destinos planejados com suas respectivas datas e orçamentos.
5. Pesquisar Destino:
    - Permita ao usuário buscar por um destino e exibir suas informações (data e orçamento).
6. Exibir Resumo:
    - Exiba o total de destinos planejados e o orçamento total estimado.
7. Filtrar por Orçamento Máximo:
    - Permita ao usuário digitar um valor máximo de orçamento e exiba todos os destinos dentro desse limite.
8. Ordenar Destinos por Data:
    - Organize as viagens em ordem cronológica, sincronizando as listas.
9. Sair."""

from datetime import date

ano_atual = date.today().year
lista_destinos = []
lista_datas = []
lista_orcamentos = []
lista_viagem = []

while True:
    print(
        """
OPÇÕES:
[1] Adicionar Destino
[2] Remover Destino
[3] Atualizar Informações
[4] Listar Viagens
[5] Pesquisar Destino
[6] Exibir Resumo
[7] Filtrar por Orçamento Máximo
[8] Ordenar Destinos por Data
[9] Sair"""
    )

    while True:
        try:
            opcao = int(input("Escolha a opção: "))
            if 1 <= opcao <= 9:
                break
            else:
                print("Escolha uma opção entre [1] e [9].")
        except ValueError:
            print("Digite um número válido entre [1] e [9].")

    # Sair
    if opcao == 9:
        print("Finalizando o programa de planejamento de viagens. Até logo!")
        break

    # Adicionar o destino, data e orçamento
    elif opcao == 1:
        while True:
            # Localização
            while True:
                localizacao = input("Digite o destino: ").capitalize().strip()
                if not localizacao:
                    print("O destino não pode estar vazio. Tente novamente.")
                    continue
                if all(
                    localizacao.isalpha() or localizacao.isspace()
                    for localizacao in localizacao
                ):
                    break
                else:
                    print(
                        "O destino deve conter apenas letras e espaços. Tente novamente."
                    )
                    continue

            # Data
            while True:
                data_viagem = input("Digite a data da viagem (dd/mm/aaaa): ").strip()
                try:
                    dia, mes, ano = map(int, data_viagem.split("/")) >= ano_atual
                    break
                except (ValueError, AssertionError):
                    print("Data inválida. Use o formato dd/mm/aaaa.")

            # Orçamento
            while True:
                try:
                    orcamento_estimado = input("Digite o orçamento estimado R$: ")
                    orcamento_estimado = orcamento_estimado.replace(",", ".")
                    orcamento_estimado = float(orcamento_estimado)
                    if orcamento_estimado > 0:
                        break
                    else:
                        print("O orçamento deve ser um número positivo.")
                except ValueError:
                    print("Digite um número válido para o orçamento.")

            # Adicionar viagem à lista
            print(
                f"Destino: {localizacao}, Data: {data_viagem}, Orçamento: R$ {orcamento_estimado}"
            )
            confirmar = input("Deseja salvar a viagem? (s/n): ").lower().strip()[0]
            if confirmar == "s":
                lista_viagem.append([localizacao, data_viagem, orcamento_estimado])
                print(f"Viagem para {localizacao} salva com sucesso!")
            else:
                print("Viagem descartada")

            confirmar = (
                input("Deseja adicionar outra viagem? (s/n): ").lower().strip()[0]
            )
            if confirmar == "n":
                print("Voltando ao menú.")
                break

    # Remover viagem da lista
    elif opcao == 2:
        if lista_viagem:
            print("\nVIAGENS")
            for indice, (localizacao, data_viagem, orcamento_estimado) in enumerate(
                lista_viagem, start=1
            ):
                print(
                    f"{indice}. {localizacao} - Data: {data_viagem} - Orçamento: R$ {orcamento_estimado}"
                )

            while True:
                try:
                    indice_remover_viagem = int(
                        input("Digite o índice da viagem que deseja remover: ")
                    )
                    if 1 <= indice_remover_viagem <= len(lista_viagem):
                        viagem_removida = lista_viagem.pop(indice_remover_viagem - 1)
                        print(
                            f"Viagem para '{viagem_removida[0]}' removida da lista com sucesso!"
                        )
                        break
                    else:
                        print("Índice não encontrado. Insira um existente.")
                except ValueError:
                    print("Digite um número que seja válido para o índice.")

        else:
            print("A lista de viagens planejadas está vazia.")

    # Atualizar informações da viagem
    elif opcao == 3:
        if lista_viagem:
            print("\nVIAGENS")
            for indice, (localizacao, data_viagem, orcamento_estimado) in enumerate(
                lista_viagem, start=1
            ):
                print(
                    f"{indice}. {localizacao} - Data: {data_viagem} - Orçamento: R$ {orcamento_estimado}"
                )

            while True:
                opcao_atualizar = input(
                    "Deseja atualizar qual informação?\n[1] Data\n[2] Orçamento: "
                ).strip()

                if opcao_atualizar in ["1", "2"]:
                    # Pedir índice
                    while True:
                        try:
                            indice_atualizacao = int(
                                input(
                                    "Digite o índice da viagem que deseja atualizar: "
                                )
                            )
                            if 1 <= indice_atualizacao <= len(lista_viagem):
                                break
                            else:
                                print("Índice não encontrado. Tente novamente.")
                        except ValueError:
                            print("Por favor, insira um número válido.")

                    # Atualizar data
                    if opcao_atualizar == "1":
                        while True:
                            nova_data = input(
                                "Digite a nova data (dd/mm/aaaa): "
                            ).strip()
                            try:
                                dia, mes, ano = map(int, nova_data.split("/"))
                                if 1 <= dia <= 31 and 1 <= mes <= 12 and ano >= ano_atual:
                                    # ano atual
                                    lista_viagem[indice_atualizacao - 1][1] = nova_data
                                    print("Data atualizada com sucesso!")
                                    break
                            except ValueError:
                                print("Data inválida. Tente novamente.")

                    elif opcao == "2":
                        while True:
                            novo_orcamento = input(
                                "Informe o novo orçamento R$: "
                            ).strip()
                            try:
                                novo_orcamento = float(novo_orcamento.replace(",", "."))
                                lista_viagem[indice_atualizacao - 1][2] = novo_orcamento
                                print("Orçamento atualizado com sucesso!")
                                break
                            except ValueError:
                                print("Digite um orçamento válido.")

                    break

                else:
                    print("Opção inválida. Por favor digite '1' ou '2'.")


print(lista_viagem)
print(ano_atual)
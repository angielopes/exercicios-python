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
                if not localizacao.isalpha():
                    print("O destino deve conter apenas letra. Tente novamente.")
                    continue
                break

            # Data
            while True:
                data_viagem = input("Digite a data da viagem (dd/mm/aaaa): ").strip()
                try:
                    dia, mes, ano = map(int, data_viagem.split("/"))
                    assert 1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0
                    break
                except (ValueError, AssertionError):
                    print("Data inválida. Use o formato dd/mm/aaaa.")

            # Orçamento
            while True:
                try:
                    orcamento_estimado = input("Digite o orçamento estimado: ")
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
                lista_viagem.append((localizacao, data_viagem, orcamento_estimado))
                print(f"Viagem para {localizacao} salva com sucesso!")
            else:
                print("Viagem descartada")

            continuar = (
                input("Deseja adicionar outra viagem? (s/n): ").lower().strip()[0]
            )
            if confirmar == "n":
                print("Voltando ao menú.")
                break

print(lista_viagem)

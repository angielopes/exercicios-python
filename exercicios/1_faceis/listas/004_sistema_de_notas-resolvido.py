"""Crie um programa que permita gerenciar as notas de uma turma de alunos. Ele deve oferecer as seguintes opções:
1. Adicionar aluno:
    O usuário deve informar o nome do aluno e uma lista com 3 notas (usando input e conversão para números).
    O aluno será adicionado à lista no formato ["Nome", [nota1, nota2, nota3]].
2. Remover aluno:
    O usuário deve informar o nome do aluno para removê-lo da lista. Se o aluno não existir, exiba uma mensagem informativa.
3. Visualizar média de um aluno:
    O usuário deve informar o nome do aluno, e o programa calcula e exibe a média das notas.
4. Listar todos os alunos e médias:
    O programa exibe todos os alunos da lista, mostrando suas médias.
5. Sair do programa."""

sistema_notas = []

while True:
    print(
        """
          OPÇÕES:
    [1] Adicionar aluno
    [2] Remover aluno
    [3] Visualizar média de um aluno
    [4] Listar todos os alunos e médias
    [5] Sair"""
    )

    try:
        opcao = int(input("\nEscolha a opção: "))
    except ValueError:
        print("Por favor, escolha um número válido: ")
        continue

    # Sair do programa
    if opcao == 5:
        print("\nPrograma encerrado...")
        break

    # Adicionando aluno
    elif opcao == 1:
        nome_aluno = input("Insira o nome do aluno: ").title().strip()
        # Adicionando três notas do aluno
        notas_alunos = []
        for i in range(1, 4):
            while True:
                try:
                    notas = float(input(f"{i}ª nota do aluno: "))
                    if 0 <= notas <= 10:
                        notas_alunos.append(notas)
                        break
                    else:
                        print("A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Digite um alor numérico válido.")
        sistema_notas.append([nome_aluno, notas_alunos])
        print(f"{nome_aluno} adicionado.")

    # Remover aluno
    elif opcao == 2:
        remover_aluno = input("Qual aluno deseja remover? ").title().strip()
        for aluno in sistema_notas:
            if aluno[0] == remover_aluno:
                sistema_notas.remove(aluno)
                print(f"{remover_aluno} removido com sucesso!")
                break
        else:
            print(f"Aluno {remover_aluno} não encontrado.")

    # Calcular e visualizar a média do aluno
    elif opcao == 3:
        consulta_aluno_media = (
            input("Insira o nome do aluno para visualizar a média dele: ")
            .title()
            .strip()
        )
        for aluno in sistema_notas:
            if aluno[0] == consulta_aluno_media:
                media = sum(aluno[1]) / len(aluno[1])
                print(f"\n{consulta_aluno_media} tem a média {media:.2f}.")
                break
        else:
            print(f"Aluno {consulta_aluno_media} não encontrado.")

    # Listar todos os alunos e suas médias
    elif opcao == 4:
        if sistema_notas:
            print("\nLista de alunos e as suas médias:")
            for aluno in sistema_notas:
                media = sum(aluno[1]) / len(aluno[1])
                print(f"{aluno[0]} - Média: {media:.2f}")
        else:
            print("Nenhum aluno registrado.")
    else:
        (print("Opção inválida! Tente novamente."))

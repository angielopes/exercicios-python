"""Crie um programa que funcione como um gerenciador simples de tarefas. Ele deve:
1. Permitir que o usuário adicione tarefas a uma lista.
    - Cada tarefa deve ter um nome e uma prioridade (baixa, média ou alta).
    - Utilize listas para armazenar as tarefas e suas prioridades
    (pode usar uma lista de listas ou duas listas separadas).
2. Exibir todas as tarefas registradas com suas respectivas prioridades.
3. Permitir que o usuário conclua uma tarefa.
    - Ao concluir, remova a tarefa da lista e mostre a lista atualizada.
4. Se o usuário tentar concluir uma tarefa que não existe, exiba uma mensagem de erro."""

lista_tarefas = []

# Adicionando tarefas e prioridades
while True:
    tarefa = input(
        "Adicione uma tarefa (ou digite 'SAIR' para finalizar): "
    ).capitalize()
    if tarefa == "Sair":
        break
    prioridade = input(
        "Informa a prioridade da tarefa (baixa, média, alta): "
    ).capitalize()
    lista_tarefas.append([tarefa, prioridade])

print("\nTarefas registradas:")
for tarefa, prioridade in lista_tarefas:
    print(f"- {tarefa} (Prioridade: {prioridade})")

# Concluindo tarefas
concluir_tarefa = input("Digite a tarefa que foi concluída: ").capitalize()
for tarefa in lista_tarefas:
    if tarefa[0] == concluir_tarefa:
        lista_tarefas.remove(tarefa)
        print("Tarefa concluída com sucesso!")
        break
else:
    print("Essa tarefa não está na lista!")

# Tarefas pendentes
if lista_tarefas:
    print("\nTarefas pendentes:")
    for tarefa, prioridade in lista_tarefas:
        print(f"- {tarefa} (Propriedade: {prioridade})")
else:
    print("\n Todas as tarefas foram concluídas. Parabéns!")

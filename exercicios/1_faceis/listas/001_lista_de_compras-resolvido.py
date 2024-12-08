"""Crie um programa que simula uma lista de compras.
O programa deve:
1.Pedir para o usuário adicionar itens à lista de compras.
    - Continue pedindo itens até que o usuário digite "sair".
    - Não permita que o usuário adicione itens duplicados na lista.
2. Exiba a lista de compras final ordenada em ordem alfabética.
3.Peça para o usuário remover itens da lista, caso queira.
    - Continue pedindo itens para remover até que o usuário digite "parar".
    - Exiba a lista atualizada após cada remoção."""

lista_compra = []

# Adicionando itens à lista
while True:
    item_lista = input(
        "Adicione um item à lista de compras (ou digite 'SAIR' para finalizar): "
    ).lower()
    if item_lista == "sair":
        break
    elif item_lista in lista_compra:
        print("Item já adicionado!")
    else:
        lista_compra.append(item_lista)

lista_compra.sort()
print("Sua lista de compras: ", lista_compra)

# Removendo itens da lista
while True:
    remover_item = input(
        "Gostaria de remover algum item? Digite o nome do item (ou 'PARAR' para sair): "
    ).lower()
    if remover_item == "parar":
        break
    elif remover_item in lista_compra:
        lista_compra.remove(remover_item)
        print("Item removido! Lista atualizada: ", lista_compra)
    else:
        print("Este item não está na lista.")

lista_compra.sort()
print("Lista final: ", lista_compra)

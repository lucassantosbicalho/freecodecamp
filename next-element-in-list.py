def proximo_elemento_dicionario(lista, elemento):
    """Retorna o próximo elemento em uma lista circular usando um dicionário.

    Args:
        lista: A lista de elementos.
        elemento: O elemento para o qual se deseja encontrar o próximo.

    Returns:
        O próximo elemento na lista.
    """

    # Cria um dicionário para mapear cada elemento ao seu sucessor
    mapa = {lista[i]: lista[(i + 1) % len(lista)] for i in range(len(lista))}
    print(f'List {lista}')
    print(f'Mapa {mapa}')
    return mapa[elemento]

def proximo_elemento_loop(lista, elemento):
    """Retorna o próximo elemento em uma lista circular usando um loop.

    Args:
        lista: A lista de elementos.
        elemento: O elemento para o qual se deseja encontrar o próximo.

    Returns:
        O próximo elemento na lista.
    """

    for i in range(len(lista)):
        if lista[i] == elemento:
            return lista[(i + 1) % len(lista)]

# Exemplo de uso:
lista = [1, 2, 3]
print(proximo_elemento_loop(lista, 1))  # Saída: 2
print(proximo_elemento_loop(lista, 2))  # Saída: 3
print(proximo_elemento_loop(lista, 3))  # Saída: 1

# Exemplo de uso:
lista = [1, 2, 3]
print(proximo_elemento_dicionario(lista, 1))  # Saída: 2
print(proximo_elemento_dicionario(lista, 2))  # Saída: 3
print(proximo_elemento_dicionario(lista, 3))  # Saída: 1
"""
Interface entre main.py e o Grafo (algoritmos de distância).
Todas as operações do perfil Assistente passam por este módulo.
"""


def buscar_pessoa(arvore, nome):
    """
    Busca uma pessoa pelo nome na árvore BST.

    Returns:
        Objeto Pessoa se encontrado, None caso contrário.
    """
    return arvore.buscar(nome)


def menor_distancia(grafo, cidade_origem, cidade_destino):
    """
    Calcula o menor caminho entre cidade_origem e cidade_destino usando Dijkstra.

    Returns:
        (caminho, distancia)
        - caminho: lista de cidades (str) ou None se não houver caminho
        - distancia: custo total (int) ou float('inf')
    """
    return grafo.dijkstra(cidade_origem, cidade_destino)


def menor_distancia_com_intermediario(grafo, cidade_origem, intermediario, cidade_destino):
    """
    Calcula o menor caminho de cidade_origem até cidade_destino passando obrigatoriamente
    pela cidade intermediária.

    Returns:
        (caminho_completo, distancia_total)
        - caminho_completo: lista de cidades ou None
        - distancia_total: custo total ou float('inf')
    """
    return grafo.caminho_com_intermediario(cidade_origem, intermediario, cidade_destino)


def cidade_mais_proxima_com_moradores(grafo, arvore, cidade_escola):
    """
    Encontra a cidade mais próxima da escola (cidade_escola) que possui moradores
    cadastrados na lista de espera.

    Args:
        grafo        : Grafo carregado do CSV
        arvore       : ArvoreBST com as pessoas cadastradas
        cidade_escola: str - nome da cidade da escola

    Returns:
        (cidade, distancia, moradores)
        - cidade   : str ou None se não houver pessoas cadastradas
        - distancia: menor distância encontrada
        - moradores: lista de objetos Pessoa da cidade encontrada
    """
    todas_pessoas = arvore.in_order()

    if not todas_pessoas:
        return None, float('inf'), []

    # Agrupa pessoas por cidade
    cidades_com_moradores = {}
    for pessoa in todas_pessoas:
        cidade = pessoa.cidade
        if cidade not in cidades_com_moradores:
            cidades_com_moradores[cidade] = []
        cidades_com_moradores[cidade].append(pessoa)

    menor_dist = float('inf')
    cidade_mais_proxima = None

    for cidade in cidades_com_moradores:
        _, dist = grafo.dijkstra(cidade_escola, cidade)
        if dist < menor_dist:
            menor_dist = dist
            cidade_mais_proxima = cidade

    if cidade_mais_proxima is None:
        return None, float('inf'), []

    moradores = cidades_com_moradores.get(cidade_mais_proxima, [])
    return cidade_mais_proxima, menor_dist, moradores

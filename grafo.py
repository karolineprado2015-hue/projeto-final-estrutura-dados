import heapq


class Grafo:
    """
    Grafo ponderado e não-direcionado representado por lista de adjacência.
    Utiliza o algoritmo de Dijkstra para encontrar o menor caminho entre cidades.
    """

    def __init__(self):
        self.adjacencia = {}

    def adicionar_cidade(self, cidade):
        """Garante que a cidade existe no dicionário de adjacência."""
        if cidade not in self.adjacencia:
            self.adjacencia[cidade] = []

    def adicionar_aresta(self, cidade1, cidade2, distancia):
        """Adiciona uma aresta bidirecional entre duas cidades com a distância dada."""
        self.adicionar_cidade(cidade1)
        self.adicionar_cidade(cidade2)
        self.adjacencia[cidade1].append((cidade2, distancia))
        self.adjacencia[cidade2].append((cidade1, distancia))

    def cidades(self):
        """Retorna a lista de todas as cidades presentes no grafo."""
        return list(self.adjacencia.keys())

    def dijkstra(self, origem, destino):
        """
        Aplica o algoritmo de Dijkstra para encontrar o menor caminho entre origem e destino.

        Retorna:
            (caminho, distancia) onde caminho é uma lista de cidades ou None se não houver caminho,
            e distancia é o custo total (float('inf') se não houver caminho).
        """
        if origem not in self.adjacencia or destino not in self.adjacencia:
            return None, float('inf')

        if origem == destino:
            return [origem], 0

        # Inicializa distâncias com infinito
        distancias = {cidade: float('inf') for cidade in self.adjacencia}
        distancias[origem] = 0
        predecessores = {cidade: None for cidade in self.adjacencia}

        # Min-heap: (distancia_acumulada, cidade)
        heap = [(0, origem)]
        visitados = set()

        while heap:
            dist_atual, cidade_atual = heapq.heappop(heap)

            if cidade_atual in visitados:
                continue
            visitados.add(cidade_atual)

            if cidade_atual == destino:
                break

            for vizinho, peso in self.adjacencia.get(cidade_atual, []):
                if vizinho not in visitados:
                    nova_dist = dist_atual + peso
                    if nova_dist < distancias.get(vizinho, float('inf')):
                        distancias[vizinho] = nova_dist
                        predecessores[vizinho] = cidade_atual
                        heapq.heappush(heap, (nova_dist, vizinho))

        # Verifica se o destino é alcançável
        if distancias.get(destino, float('inf')) == float('inf'):
            return None, float('inf')

        # Reconstrói o caminho percorrendo os predecessores
        caminho = []
        cidade = destino
        while cidade is not None:
            caminho.append(cidade)
            cidade = predecessores[cidade]
        caminho.reverse()

        return caminho, distancias[destino]

    def caminho_com_intermediario(self, origem, intermediario, destino):
        """
        Encontra o menor caminho de 'origem' até 'destino' passando obrigatoriamente
        por 'intermediario'.

        Retorna:
            (caminho_completo, distancia_total) ou (None, float('inf')) se não houver caminho.
        """
        caminho1, dist1 = self.dijkstra(origem, intermediario)
        caminho2, dist2 = self.dijkstra(intermediario, destino)

        if caminho1 is None or caminho2 is None:
            return None, float('inf')

        # Une os dois caminhos removendo a duplicata do intermediário
        caminho_completo = caminho1 + caminho2[1:]
        distancia_total = dist1 + dist2

        return caminho_completo, distancia_total

import csv
import random
from grafo import Grafo


def carregar_grafo_e_cidades(caminho_csv='cidades_vizinhas.csv'):
    """
    Lê o arquivo CSV (formato: cidade1;cidade2;distancia) e retorna:
        - grafo: objeto Grafo com todas as arestas carregadas
        - cidades: lista com todas as cidades únicas encontradas
    """
    grafo = Grafo()
    cidades = set()

    with open(caminho_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if len(row) >= 3:
                try:
                    cidade1 = row[0].strip()
                    cidade2 = row[1].strip()
                    distancia = int(row[2].strip())
                    if cidade1 and cidade2 and distancia > 0:
                        grafo.adicionar_aresta(cidade1, cidade2, distancia)
                        cidades.add(cidade1)
                        cidades.add(cidade2)
                except (ValueError, IndexError):
                    continue  # Ignora linhas malformadas

    return grafo, list(cidades)


def cidade_aleatoria(cidades):
    """Seleciona e retorna uma cidade aleatória da lista."""
    return random.choice(cidades)

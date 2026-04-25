"""
Interface entre main.py e a estrutura de dados Lista Encadeada.
Todas as operações do perfil Secretário(a) passam por este módulo.
"""

import random
from pessoa import Pessoa


def adicionar_pessoa(lista, nome, idade, telefone, cidades):
    """
    Cria uma Pessoa com cidade atribuída aleatoriamente e insere na lista encadeada.

    Args:
        lista   : ListaEncadeada
        nome    : str
        idade   : int
        telefone: str
        cidades : list[str] - lista de cidades carregadas do CSV

    Returns:
        Pessoa recém-criada e inserida
    """
    cidade = random.choice(cidades)
    pessoa = Pessoa(nome, idade, telefone, cidade)
    lista.inserir(pessoa)
    return pessoa


def buscar_pessoa(lista, nome):
    """
    Busca uma pessoa pelo nome na lista encadeada.

    Returns:
        Objeto Pessoa se encontrado, None caso contrário.
    """
    return lista.buscar(nome)


def contar_pessoas(lista):
    """
    Retorna a quantidade de pessoas cadastradas na lista de espera.

    Returns:
        int
    """
    return lista.contar()


def exibir_lista(lista):
    """Exibe todas as pessoas da lista de espera."""
    lista.exibir()

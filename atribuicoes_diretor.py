"""
Interface entre main.py e a estrutura de dados Árvore Binária de Busca (BST).
Todas as operações do perfil Diretor(a) passam por este módulo.
"""

from arvore_bst import ArvoreBST


def gerar_arvore(lista):
    """
    Gera e retorna uma Árvore Binária de Busca a partir da lista encadeada.
    A chave de cada nó é o nome da pessoa.

    Args:
        lista: ListaEncadeada com os dados cadastrados pelo secretário

    Returns:
        ArvoreBST populada
    """
    arvore = ArvoreBST()
    for pessoa in lista.listar_todos():
        arvore.inserir(pessoa)
    return arvore


def buscar_pessoa(arvore, nome):
    """
    Busca uma pessoa pelo nome na árvore BST.

    Returns:
        Objeto Pessoa se encontrado, None caso contrário.
    """
    return arvore.buscar(nome)


def editar_nome(arvore, nome_atual, novo_nome):
    """
    Altera o nome de uma pessoa (remove e re-insere no BST para manter a ordenação).

    Returns:
        True se alterado com sucesso, False se pessoa não encontrada.
    """
    return arvore.atualizar_nome(nome_atual, novo_nome)


def editar_idade(arvore, nome, nova_idade):
    """
    Altera a idade de uma pessoa.

    Returns:
        True se alterado com sucesso, False se pessoa não encontrada.
    """
    return arvore.atualizar_idade(nome, nova_idade)


def editar_telefone(arvore, nome, novo_telefone):
    """
    Altera o telefone de uma pessoa.

    Returns:
        True se alterado com sucesso, False se pessoa não encontrada.
    """
    return arvore.atualizar_telefone(nome, novo_telefone)


def descadastrar_pessoa(arvore, nome):
    """
    Remove uma pessoa da árvore BST.

    Returns:
        Objeto Pessoa removido, ou None se não encontrado.
    """
    return arvore.remover(nome)


def primeiro_alfabetico(arvore):
    """
    Retorna a pessoa cujo nome é o primeiro em ordem alfabética (nó mais à esquerda).

    Returns:
        Objeto Pessoa ou None se a árvore estiver vazia.
    """
    return arvore.minimo()


def ultimo_alfabetico(arvore):
    """
    Retorna a pessoa cujo nome é o último em ordem alfabética (nó mais à direita).

    Returns:
        Objeto Pessoa ou None se a árvore estiver vazia.
    """
    return arvore.maximo()

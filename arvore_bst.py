class NoArvore:
    """Nó da árvore binária de busca."""

    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.esquerdo = None
        self.direito = None


class ArvoreBST:
    """
    Árvore Binária de Busca (BST).
    A chave de ordenação é o nome da pessoa (comparação case-insensitive).
    """

    def __init__(self):
        self.raiz = None

    # ------------------------------------------------------------------ inserir
    def inserir(self, pessoa):
        """Insere uma pessoa na árvore."""
        self.raiz = self._inserir(self.raiz, pessoa)

    def _inserir(self, no, pessoa):
        if no is None:
            return NoArvore(pessoa)
        if pessoa.nome.lower() < no.pessoa.nome.lower():
            no.esquerdo = self._inserir(no.esquerdo, pessoa)
        elif pessoa.nome.lower() > no.pessoa.nome.lower():
            no.direito = self._inserir(no.direito, pessoa)
        return no

    # ------------------------------------------------------------------- buscar
    def buscar(self, nome):
        """Busca uma pessoa pelo nome. Retorna o objeto Pessoa ou None."""
        return self._buscar(self.raiz, nome)

    def _buscar(self, no, nome):
        if no is None:
            return None
        if nome.lower() == no.pessoa.nome.lower():
            return no.pessoa
        elif nome.lower() < no.pessoa.nome.lower():
            return self._buscar(no.esquerdo, nome)
        else:
            return self._buscar(no.direito, nome)

    # ------------------------------------------------------------------ remover
    def remover(self, nome):
        """Remove uma pessoa da árvore. Retorna o objeto Pessoa removido ou None."""
        self.raiz, removido = self._remover(self.raiz, nome)
        return removido

    def _remover(self, no, nome):
        if no is None:
            return None, None

        if nome.lower() < no.pessoa.nome.lower():
            no.esquerdo, removido = self._remover(no.esquerdo, nome)
        elif nome.lower() > no.pessoa.nome.lower():
            no.direito, removido = self._remover(no.direito, nome)
        else:
            # Nó encontrado
            removido = no.pessoa
            if no.esquerdo is None:
                return no.direito, removido
            elif no.direito is None:
                return no.esquerdo, removido
            # Dois filhos: substituir pelo sucessor em-ordem (menor da subárvore direita)
            successor_no = self._minimo_no(no.direito)
            no.pessoa = successor_no.pessoa
            no.direito, _ = self._remover(no.direito, successor_no.pessoa.nome)

        return no, removido

    # --------------------------------------------------------------- mín / máx
    def _minimo_no(self, no):
        while no.esquerdo is not None:
            no = no.esquerdo
        return no

    def minimo(self):
        """Retorna a pessoa com o nome alfabeticamente primeiro. Retorna None se vazia."""
        if self.raiz is None:
            return None
        return self._minimo_no(self.raiz).pessoa

    def _maximo_no(self, no):
        while no.direito is not None:
            no = no.direito
        return no

    def maximo(self):
        """Retorna a pessoa com o nome alfabeticamente último. Retorna None se vazia."""
        if self.raiz is None:
            return None
        return self._maximo_no(self.raiz).pessoa

    # ----------------------------------------------------------- percurso em-ordem
    def in_order(self):
        """Retorna lista de objetos Pessoa em ordem alfabética."""
        resultado = []
        self._in_order(self.raiz, resultado)
        return resultado

    def _in_order(self, no, resultado):
        if no is not None:
            self._in_order(no.esquerdo, resultado)
            resultado.append(no.pessoa)
            self._in_order(no.direito, resultado)

    # ------------------------------------------------------------------ atualizar
    def atualizar_nome(self, nome_atual, novo_nome):
        """Atualiza o nome de uma pessoa (precisa re-inserir na árvore). Retorna True/False."""
        pessoa = self.buscar(nome_atual)
        if pessoa is None:
            return False
        self.remover(nome_atual)
        pessoa.nome = novo_nome
        self.inserir(pessoa)
        return True

    def atualizar_idade(self, nome, nova_idade):
        """Atualiza a idade de uma pessoa in-place. Retorna True/False."""
        pessoa = self.buscar(nome)
        if pessoa is None:
            return False
        pessoa.idade = nova_idade
        return True

    def atualizar_telefone(self, nome, novo_telefone):
        """Atualiza o telefone de uma pessoa in-place. Retorna True/False."""
        pessoa = self.buscar(nome)
        if pessoa is None:
            return False
        pessoa.telefone = novo_telefone
        return True

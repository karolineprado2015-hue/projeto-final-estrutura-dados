class No:
    """Nó da lista encadeada simples."""

    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.proximo = None


class ListaEncadeada:
    """Lista encadeada simples para armazenar pessoas na lista de espera."""

    def __init__(self):
        self.cabeca = None
        self._tamanho = 0

    def inserir(self, pessoa):
        """Insere uma pessoa no final da lista."""
        novo_no = No(pessoa)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
        self._tamanho += 1

    def buscar(self, nome):
        """Busca uma pessoa pelo nome (case-insensitive). Retorna o objeto Pessoa ou None."""
        atual = self.cabeca
        while atual is not None:
            if atual.pessoa.nome.lower() == nome.lower():
                return atual.pessoa
            atual = atual.proximo
        return None

    def remover(self, nome):
        """Remove uma pessoa da lista pelo nome. Retorna True se removida, False caso contrário."""
        if self.cabeca is None:
            return False
        if self.cabeca.pessoa.nome.lower() == nome.lower():
            self.cabeca = self.cabeca.proximo
            self._tamanho -= 1
            return True
        atual = self.cabeca
        while atual.proximo is not None:
            if atual.proximo.pessoa.nome.lower() == nome.lower():
                atual.proximo = atual.proximo.proximo
                self._tamanho -= 1
                return True
            atual = atual.proximo
        return False

    def contar(self):
        """Retorna a quantidade de pessoas na lista."""
        return self._tamanho

    def listar_todos(self):
        """Retorna uma lista Python com todos os objetos Pessoa."""
        pessoas = []
        atual = self.cabeca
        while atual is not None:
            pessoas.append(atual.pessoa)
            atual = atual.proximo
        return pessoas

    def exibir(self):
        """Exibe todas as pessoas da lista formatadas."""
        if self.cabeca is None:
            print("  (lista vazia)")
            return
        atual = self.cabeca
        i = 1
        while atual is not None:
            print(f"  {i}. {atual.pessoa.linha_resumida()}")
            atual = atual.proximo
            i += 1

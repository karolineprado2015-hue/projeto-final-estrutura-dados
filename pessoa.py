class Pessoa:
    """Representa uma pessoa na lista de espera da escola."""

    def __init__(self, nome, idade, telefone, cidade):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cidade = cidade

    def __str__(self):
        return (
            f"  Nome    : {self.nome}\n"
            f"  Idade   : {self.idade} anos\n"
            f"  Telefone: {self.telefone}\n"
            f"  Cidade  : {self.cidade}"
        )

    def linha_resumida(self):
        return f"[{self.nome} | {self.idade} anos | Tel: {self.telefone} | Cidade: {self.cidade}]"

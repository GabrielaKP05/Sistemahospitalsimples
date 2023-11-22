class Mae:
    def __init__(self, nome, endereco, telefone, data_nascimento):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.data_nascimento = data_nascimento

    # getters
    def get_nome(self):
        return self.nome

    # setters
    def set_nome(self, nome):
        self.nome = nome


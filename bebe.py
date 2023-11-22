class Bebe:
    def __init__(self, nome, data_nascimento, peso_nascimento, altura, mae, medico):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.peso_nascimento = peso_nascimento
        self.altura = altura
        self.mae = mae
        self.medico = medico

    # getters
    def get_nome(self):
        return self.nome

    # setters
    def set_nome(self, nome):
        self.nome = nome
  

class Medico:
    def __init__(self, CRM, nome, telefone_celular, especialidade):
        self.CRM = CRM
        self.nome = nome
        self.telefone_celular = telefone_celular
        self.especialidade = especialidade

    # getters
    def get_nome(self):
        return self.nome

    # setters
    def set_nome(self, nome):
        self.nome = nome


class Ingresso:
    def __init__(self, nome, sessao, id):
        self.nome = nome
        self.sessao = sessao
        self.id = id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_sessao(self):
        return self.sessao

    def set_sessao(self, sessao):
        self.sessao = sessao

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

class Sessao:
    def __init__(self, sessao, horario, filme, sala):
        self.__sessao = sessao
        self.__horario = horario
        self.__filme = filme
        self.__sala = sala


    def get_sessao(self):
        return self.__sessao

    def set_sessao(self, nova_sessao):
        self.__sessao = nova_sessao

    def get_horario(self):
        return self.__horario

    def set_horario(self, novo_horario):
        self.__horario = novo_horario

    def get_filme(self):
        return self.__filme.get_nome()

    def set_filme(self, filme):
        self.__filme = filme

    def get_sala(self):
        return self.__sala.get_numero_da_sala()

    def set_sala(self, sala):
        self.__sala = sala
from Admin import Admin

class Cliente(Admin):
    def __init__(self, nome, email, telefone, senha, id):
        super().__init__(nome, email, telefone, senha)
        self.__id = id

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

class Assento:
    def __init(self, numero, fila):
        self.numero = numero
        self.fila = fila

    def get_numero(self):
        return self.numero

    def set_numero(self, numero):
        self.numero = numero

    def get_fila(self):
        return self.fila

    def set_fila(self, nova_fila):
        self.__fila = nova_fila
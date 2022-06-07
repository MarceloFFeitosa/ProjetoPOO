class Sala:
        def __init__(self, numero_da_sala, numero_de_assentos):
                self.numero_da_sala = numero_da_sala
                self.numero_de_assentos = numero_de_assentos

        def get_numero_da_sala(self):
            return self.numero_da_sala
        def set_numero_da_sala(self, novo_numero_da_sala):
                    self.numero_da_sala = novo_numero_da_sala
        def get_numero_de_assentos(self):
            return self.numero_de_assentos
        def set_numero_de_assentos(self, novo_numero_de_assentos):
                self.numero_de_assentos = novo_numero_de_assentos

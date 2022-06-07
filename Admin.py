from Usuario import Usuario

class Admin(Usuario):
    def __init__(self, nome, email, telefone, usuario, senha):
        super().__init__(nome, email, telefone, usuario, senha)

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_telefone(self):
        return self.telefone

    def set_telefone(self, telefone):
        self.telefone = telefone

    def get_senha(self):
        return self.senha

    def set_senha(self, senha):
        self.senha = senha

    def cadastrar_filme(self, filme, lista_de_filmes):
        lista_de_filmes.append(filme)

    def cadastrar_usuario(self, usuario, lista_de_usuarios):
        lista_de_usuarios.append(usuario)

    def remover_filme(self, nome, lista_de_filmes):
        for filme in lista_de_filmes:
            if filme.get_nome().lower() == nome.lower():
                lista_de_filmes.remove(filme)
                return "Filme removido com sucesso!"
            else:
                return "Filme não encontrado"

    def cadastrar_sala(self, sala, lista_de_salas):
        lista_de_salas.append(sala)

    def remover_sala(self, nome, lista_de_salas):
        for sala in lista_de_salas:
            if sala.get_numero_da_sala().lower() == nome.lower():
                lista_de_salas.remove(sala)
                return "Sala removida com sucesso!"
            else:
                return "Sala não encontrada"

    def cadastrar_cliente(self, cliente, lista_de_clientes):
        lista_de_clientes.append(cliente)

    def remover_sessao(self, numero, lista_de_sessoes):
        for sessao in lista_de_sessoes:
            if sessao.get_sessao().lower() == numero.lower():
                lista_de_sessoes.remove(sessao)
                return "Sessão removida com sucesso!"
            else:
                return "Sessão não encontrada"
    


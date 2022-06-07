class Usuario:
    def __init__(self, nome, email, telefone, usuario, senha):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__usuario = usuario
        self.__senha = senha

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_usuario(self):
        return self.__usuario

    def set_usuario(self, new_usuario):
        self.__usuario = new_usuario

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha):
        self.__senha = senha

    def listar_filmes(self, lista_de_filmes):
        lista = []
        for filme in lista_de_filmes:
            if filme.get_nome() and filme.get_diretor() and filme.get_duracao() and filme.get_descricao():
                lista.append(
                    f'Nome: {filme.get_nome()}, Diretor: {filme.get_diretor()}, Duração: {filme.get_duracao()}, Descrição: {filme.get_descricao()}')

        return lista

    def pesquisar_filme(self, nome, lista_de_filmes):
        for filme in lista_de_filmes:
            if filme.get_nome().lower() == nome.lower():
                return "Nome: " + filme.get_nome() + "\n" + "Diretor: " + filme.get_diretor() + "\n" + "Duração: " + filme.get_duracao() + "\n" + "Descrição: " + filme.get_descricao()
            else:
                return 'Filme não encontrado!'

    def listar_sala(self, lista_de_salas):
        lista = []
        for sala in lista_de_salas:
            if sala.get_numero_da_sala() and sala.get_numero_de_assentos():
                lista.append(
                    f'Numero da sala: {sala.get_numero_da_sala()}, Quantidade de assentos: {sala.get_numero_de_assentos()}')

        return lista

    def pesquisar_sala(self, numero, lista_de_salas):
        for sala in lista_de_salas:
            if sala.get_numero_da_sala().lower() == numero.lower():
                return "SALA: " + sala.get_numero_da_sala() + "\n" + "Quantidade de assentos: " + sala.get_numero_de_assentos()
            else:
                return 'Sala não encontrada!'

    def listar_sessao(self, lista_de_sessoes):
        lista = []
        for sessao in lista_de_sessoes:
            if sessao.get_sessao():
                lista.append(
                    f'Numero da sessão: {sessao.get_sessao()}, Filme: {sessao.get_filme()}, Sala: {sessao.get_sala()}, Horário: {sessao.get_horario()}')
        return lista
    def pesquisar_sessao(self, numero, lista_de_sessoes):
        for sessao in lista_de_sessoes:
            if sessao.get_sessao.lower() == numero.lower():
                return "Sessão: " + sessao.get_sessao() + "\n" + "Horario " + sessao.get_horario() + "\n" + "Filme: " + sessao.get_filme()
            else:
                return 'Sessão não encontrada!'



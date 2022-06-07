from Admin import Admin
from Filme import Filme
from Sala import Sala
from Usuario import Usuario
from Sessao import Sessao
from Ingresso import Ingresso
import uuid

lista_de_filmes = []
lista_de_salas = []
teste = Admin("Gustavo", "email.com", "799999999", "GMBOSS", "Teste123")
lista_de_clientes = []
lista_de_sessoes = []
lista_de_ingressos = []

filme1 = Filme("Homem Aranha", "Jon Watts", "02:30:00", "Filme do miranha")
filme2 = Filme("Harry Potter", "Cris Collombus", "01:30:45", "Filme do harry")
sala1 = Sala("1", "50")
sessao1 = Sessao("1", "15:30", filme1, sala1)
sessao2 = Sessao("2", "19:00", filme2, sala1)

lista_de_filmes.append(filme1)
lista_de_filmes.append(filme2)
lista_de_salas.append(sala1)
lista_de_sessoes.append(sessao1)

opc = True


def login():
    try:
        print("-----------------BEM VINDO AO CINEMANIA---------------------")
        print("------------DIGITE A OPCAO QUE DESEJA REALIZAR--------------")
        print("""
              1 - Login como Administrador
              2 - Login/Cadastro Cliente
              3 - Sair
              """)
        print("------------------------------------------------------------")
        opc = input("")

        if opc == "1":
            print("--------Login ADM--------")
            user = input("Usuario: ")
            senha = input("Senha: ")
            if user.lower() == "gmboss" and senha == "Teste123":
                print("--------Logado com sucesso-------")
                opc2 = True
                while opc2:
                    print("""
                          1.Cadastrar novo Filme
                          2.Apagar Filme
                          3.Ver Filmes
                          4.Pesquisar Filme
                          5.Cadastrar nova Sala
                          6.Apagar Sala
                          7.Ver Salas
                          8.Pesquisar Sala
                          9.Cadastrar Sessão
                          10.Apagar Sessão
                          11.Ver Sessão
                          12.Pesquisar Sessão
                          0.Sair
                          """)
                    opc2 = input("O que vc quer fazer? ")
                    if opc2 == "1":
                        print("--------CADASTRAR DE FILME--------")
                        titulo = input("Digite o nome do filme: ")
                        diretor = input("Digite o diretor do filme: ")
                        duracao = input("Digite a duraçao do filme: ")
                        descricao = input("Digite a descrição do filme: ")
                        if titulo and diretor and duracao and descricao:
                            filme_cadastrado = Filme(titulo, diretor, duracao, descricao)
                            teste.cadastrar_filme(filme_cadastrado, lista_de_filmes)

                            print("Filme cadastrado!!")
                        else:
                            print("Filme não cadastrado! Tente novamente. Preencha todos os campos!")

                    elif opc2 == "2":
                        print("--------APAGAR FILME--------")
                        nome = input("Digite o nome do filme que quer apagar: ")
                        if nome:
                            print(teste.remover_filme(nome, lista_de_filmes))
                        else:
                            print("Digite o nome do filme para remover!")
                    elif opc2 == "3":
                        print("--------VER FILMES--------")
                        print(teste.listar_filmes(lista_de_filmes))
                    elif opc2 == "4":
                        print("--------PESQUISAR FILME--------")
                        nome = input("Digite o nome do filme: ")
                        if nome:
                            print(teste.pesquisar_filme(nome, lista_de_filmes))
                        else:
                            print("Digite o nome do filme para pesquisar!")
                    elif opc2 == "5":
                        print("--------CADASTRAR SALA--------")
                        sala = input("Digite o numero da Sala: ")
                        numero = input("Digite a quantidade de assentos: ")
                        if sala and numero:
                            sala_cadastrada = Sala(sala, numero)
                            teste.cadastrar_sala(sala_cadastrada, lista_de_salas)
                            print("Sala cadastrada com sucesso!!")
                        else:
                            print("Sala não cadastrada! Tente novamente. Preencha todos os campos!")
                    elif opc2 == "6":
                        print("--------APAGAR SALA--------")
                        sala = input("Digite o numero da sala que quer apagar: ")
                        if sala:
                            print(teste.remover_sala(sala, lista_de_salas))
                        else:
                            print("Digite o numero da sala para remover!")
                    elif opc2 == "7":
                        print("--------VER SALAS--------")
                        print(teste.listar_sala(lista_de_salas))
                    elif opc2 == "8":
                        print("--------PESQUISAR SALA--------")
                        numero = input("Digite o numero da sala: ")
                        if numero:
                            print(teste.pesquisar_sala(numero, lista_de_salas))
                        else:
                            print("Digite o numero da sala para pesquisar!")
                    
                    elif opc2 == "9":
                        print("--------CADASTRAR SESSÃO--------")
                        valor_sessao = input("Digite a sessão: ")
                        horario_sessao = input("Digite o horário da sessão: ")                       
                        print('Escolha um filme\n\n')
                        print("---------FILMES DISPONIVEIS--------")
                        opcao = 0
                        for filme in lista_de_filmes:
                            print(f'Nome do filme: {filme.get_nome()}, Opção {opcao}')
                            opcao += 1
                        opcao_escolhida = int(input("Escolher opcao: "))
                        if opcao_escolhida >= 0 and opcao_escolhida <= int(len(lista_de_filmes)):
                                print(f'Filme escolhido: {lista_de_filmes[opcao_escolhida].get_nome()}')
                                filme_escolhido = lista_de_filmes[opcao_escolhida]
                                print("---------Salas DISPONIVEIS--------")
                                opcao_sala = 0
                                for sala in lista_de_salas:
                                    print(f'Numero da sala: {sala.get_numero_da_sala()}, Opção {opcao_sala}')
                                    opcao_sala += 1
                                opcao_escolhida = int(input("Escolher opcao: "))
                                if opcao_escolhida >= 0 and opcao_escolhida <= int(len(lista_de_salas)):
                                        sala_cad = lista_de_salas[opcao_escolhida]
                                        print(f'sala escolhida: {lista_de_salas[opcao_escolhida].get_numero_da_sala()}')
                                        sessao_cadastrada = Sessao(valor_sessao, horario_sessao, filme_escolhido, sala_cad)
                                        lista_de_sessoes.append(sessao_cadastrada)
                                        print('Sessão cadastrada com sucesso!!!')
                                else:
                                    print('Erro ao cadastrar sessão')
                        else:
                                print('Opção inválida!')

                    elif opc2 == "10":
                        print("--------APAGAR SESSÃO--------")
                        opc_excluir = input("Digite o numero da sessão que quer apagar: ")
                        if opc_excluir:
                            print(teste.remover_sessao(opc_excluir, lista_de_sessoes))
                        else:
                            print("Digite o numero da sessão para remover!")
                    elif opc2 == "11":
                        print("--------VER SESSÕES--------")
                        print(teste.listar_sessao(lista_de_sessoes))
                    elif opc2 == "12":
                        print("--------PESQUISAR SESSÃO--------")
                        numero = input("Digite o numero do sessão: ")
                        if numero != '':
                            print(teste.pesquisar_sessao(numero, lista_de_sessoes))
                        else:
                            print("Digite o numero da sessão para pesquisar!")


                    elif opc2 == "0":
                        print("--------SAINDO--------")
                        opc2 = None
                        login()
                    else:
                        print("DIGITE UMA OPCAO VALIDA!!!")
                        login()
            else:
                print("\nUSUARIO OU SENHA INCORRETO\n")
                login()

        elif opc == "2":

            print("--------LOGIN/CADASTRO CLIENTE--------")
            print("""
                1.Cadastrar
                2.Logar
                0.Voltar
                """)
            opc_cliente = input("O que deseja fazer? ")
            if opc_cliente == "1":
                print("--------CADASTRO CLIENTE--------")
                nome = input("Digite o seu nome: ")
                email = input("Digite o seu email: ")
                telefone = input("Digite o seu telefone: ")
                usuario = input("Digite o seu usuario: ")
                senha = input("Digite a sua senha: ")

                if nome and email and telefone and usuario and senha:
                    cliente_cadastrado = Usuario(nome, email, telefone, usuario, senha)
                    validador = True
                    for cliente in lista_de_clientes:
                        if cliente.get_usuario().lower == usuario.lower():
                            print("Usuario ja cadastrado")
                            validador = False
                    if validador:
                        lista_de_clientes.append(cliente_cadastrado)
                        print("Cliente cadastrado!!")

                else:
                    print("Cliente não cadastrado! Tente novamente. Preencha todos os campos!")
                login()
            elif opc_cliente == "2":
                print("--------Login CLIENTE--------")
                user = input("Usuario: ")
                senha = input("Senha: ")
                for usuario in lista_de_clientes:
                    if user == usuario.get_usuario() and senha == usuario.get_senha():
                        print("BEM VINDO " + user.upper())
                        opc3 = True
                        while opc3:
                            print("""
                                  1.Lista de Filmes
                                  2.Pesquisar Filme
                                  3.Escolher Filme
                                  4.Ver seus ingressos
                                  0.Sair
                                  """)
                            opc3 = input("Digite uma opcao: ")
                            if opc3 == "1":
                                print("---------FILMES DISPONIVEIS--------")
                                print(teste.listar_filmes(lista_de_filmes))
                            elif opc3 == "2":
                                nome = input("Digite o nome do filme: ")
                                if nome:
                                    print(teste.pesquisar_filme(nome, lista_de_filmes))
                                else:
                                    print("Digite o nome do filme para pesquisar!")
                            elif opc3 == "3":
                                print("---------FILMES DISPONIVEIS--------")
                                opcao = 0
                                for filme in lista_de_filmes:
                                    print(f'Nome do filme: {filme.get_nome()}, Opção {opcao}')
                                    opcao += 1
                                opcao_escolhida = int(input("Escolher opcao: "))
                                if opcao_escolhida >= 0 and opcao_escolhida <= int(len(lista_de_filmes)):
                                    print(f'Filme escolhido: {lista_de_filmes[opcao_escolhida].get_nome()}')
                                    for sessao in lista_de_sessoes:
                                        if sessao.get_filme().lower() == lista_de_filmes[opcao_escolhida].get_nome().lower():
                                            print(f'Disponível na sessão: {sessao.get_sessao()}, no horário: {sessao.get_horario()}, sala: {sessao.get_sala()}')
                                            deseja_comprar = input('Deseja comprar um ingresso? Digite 1 para Sim ou 0 para Não')
                                            if deseja_comprar == "1":
                                                print('Ingresso adquirido com sucesso')
                                                ingresso = Ingresso(usuario.get_nome(), sessao.get_sessao(), uuid.uuid4())
                                                lista_de_ingressos.append(ingresso)
                                            else:
                                                print("Comppra cancelada! :-(")


                                else:
                                    print("Informe uma opção válida")

                            elif opc3 == "4":
                                if len(lista_de_ingressos) > 0: 
                                    for ingresso in lista_de_ingressos:
                                        if ingresso.get_nome().lower() == usuario.get_nome().lower():
                                            print(f'Código do seu ingresso: {ingresso.get_id()}')
                                else:
                                    print('Você não possui nenhum ingresso!')
                            elif opc3 == "0":
                                print("SAINDO")
                                opc3 = None
                            else:
                                print("DIGITE UMA OPCAO VALIDA")
                                login()
                    else:
                        print("\nUSUARIO OU SENHA INCORRETO\n")
                        login()
            elif opc_cliente == "0":
                login()
            else:
                print("Informe uma opcao valida!")
                login()
        elif opc == "3":
            print("SAINDO")
            quit()

        else:
            print("DIGITE UMA OPCAO VALIDA")

    except ValueError:
        exit("APENAS NUMEROS AQUI")

    else:
        print("\n")


login()

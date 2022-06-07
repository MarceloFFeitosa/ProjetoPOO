
                print("Informe uma opcao valida!")
                login()
        elif opc == "3":
            print("SAINDO")
            quit()

        else:
            print("DIGITE UMA OPCAO VALIDA")

    except ValueError:
        exit("APENAS NUMEROS AQUI")
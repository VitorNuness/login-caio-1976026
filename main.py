from bib import *

while True:
    login = menu()
    if login == 1:
        entrar()

    elif login == 2:
        cadastrar_usuario()
    else:
        break

from dataclasses import dataclass
from getpass import getpass
from hashlib import sha256

@dataclass
class Usuario:
    user: str
    senha: str

def menu():
    opcoes = [1,2,0]
    while True:
        try:
            print("MENU\n1 - Entrar\n2 - Cadastrar\n0 - Sair")
            selecao = int(input("Opção: "))
            if selecao in opcoes:
                if selecao == 0:
                    print("Até mais.")
                    return None
                else:
                    return selecao
            else:
                print("Opção inválida.")
        except ValueError:
            print("Opção inválida.")

def cadastrar_usuario():
    while True:
        print("Digite 0 para voltar.")
        usuario = input("USUÁRIO: ").lower()
        if usuario == "0":
            break
        else:
            senha = getpass("SENHA: ")
            senha = str(sha256(senha.encode()).digest())
            if senha == "0":
                break
            else:
                arquivo_usuarios = open("usuarios.txt", "r")
                for item in arquivo_usuarios:
                    usuarios = item.split(";")
                    obj_usuario = Usuario(usuarios[0], usuarios[1])
                    if usuario == obj_usuario.user:
                        return print("Usuário já existe.")
                #lista_usuarios.append(Usuario(usuario, senha))
                with open('usuarios.txt', '+a') as arquivo:
                    arquivo.write(usuario+";"+senha+";"+"\n")                    
        return print("Cadastro realizado com sucesso.")

def abrir_arquivo(): # Ainda não funciona
    arquivo_usuarios = open("usuarios.txt", "r")
    for item in arquivo_usuarios:
        usuarios = item.split(";")
        obj_usuario = Usuario(usuarios[0], usuarios[1])
    return obj_usuario

def entrar():
    while True:
        print("Digite 0 para voltar.")
        usuario = input("USUÁRIO: ").lower()
        if usuario == "0":
            break
        else:
            senha = getpass("SENHA: ")
            senha = str(sha256(senha.encode()).digest())
            if senha == "0":
                break
            else:
                arquivo_usuarios = open("usuarios.txt", "r")
                for item in arquivo_usuarios:
                    usuarios = item.split(";")
                    obj_usuario = Usuario(usuarios[0], usuarios[1])
                    if usuario == obj_usuario.user and senha == obj_usuario.senha:
                        print(f"Olá, {usuario.capitalize()}!")
                        while True:
                            try:
                                sair = int(input("Digite 0 para sair.\n"))
                                if sair == 0:
                                    return print("Até mais.")
                            except ValueError:
                                print("Opção inválida")
        return print("Usuário não encontrado!")
    return None


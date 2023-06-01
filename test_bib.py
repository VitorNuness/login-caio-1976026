import unittest
from unittest.mock import patch
from bib import *

class TestMenu(unittest.TestCase):

    def test_menu_isnt_list_and_1(self):
        inputs = iter([
            "a",
            "1"
        ])
        with patch('builtins.input', lambda *_: next(inputs)):
            self.assertEqual(menu(), "1")
        
    @patch('builtins.input', lambda *_:"2")
    def test_menu_2(self):
        self.assertEqual(menu(), "2")

    @patch('builtins.input', lambda *_:"0")
    def test_menu_0(self):
        self.assertEqual(menu(), None)
        

class TestCadastrarUsuario(unittest.TestCase):

    @patch('builtins.input', lambda *_:"0")
    def test_cadastrar_usuario_0(self):
        self.assertEqual(cadastrar_usuario(), None)
    
    @patch('bib.getpass', lambda *_:"123")
    def test_cadastrar_usuario_sem_arquivo(self):
        inputs = iter([
            "VITOR",
            "123"
        ])
        with patch('builtins.input', lambda *_: next(inputs)):
            self.assertEqual(cadastrar_usuario(), None)

    @patch('bib.getpass', lambda *_:"123")
    def test_cadastrar_usuario_com_arquivo(self):
        inputs = iter([
            "VITOR",
            "123"
        ])
        with patch('builtins.input', lambda *_: next(inputs)):
            self.assertEqual(cadastrar_usuario(), None)

class TestEntar(unittest.TestCase):

    def setUp(self) -> None:
        try:
            os.remove("usuarios.txt")
        except:
            pass

    @patch('builtins.input', lambda *_:"0")
    def test_entrar_usuario_0(self):
        self.assertEqual(entrar(), None)

    @patch('bib.getpass', lambda *_:"123")
    def test_entrar_arquivo_nao_existe(self):
        inputs = iter([
            "VITOR",
            "123"
        ])
        with patch('builtins.input', lambda *_: next(inputs)):
            self.assertEqual(entrar(), None)

    @patch('bib.getpass', lambda *_:"123")
    def test_entrar_usuario(self):

        with open('usuarios.txt', '+a') as arquivo:
            arquivo.write('vitor'+";"+str(sha256("123".encode()).digest())+";"+"\n")

        inputs = iter([
            "VITOR",
            "123",
            "a",
            "0"
        ])
        with patch('builtins.input', lambda *_: next(inputs)):
            self.assertEqual(entrar(), None)
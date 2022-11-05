import os
import sqlite3
from sqlite3 import Error

##Conexão
def conexaoBanco():
    caminho = 'C:\\Users\\usuario\\Desktop\\Python\Projeto\\agenda.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = conexaoBanco()

def menuPrincipal():
    os.system("csl")
    print('1 - Inserir Novo Contato')
    print('2 - Deletar Contato')
    print('3 - Atualizar Contato ')
    print('4 - Consultar registro por Nome')
    print('5 - Sair')

def menuInserir():
    print()

def menuDeletar():
    print()
 
def menuAtualizar():
    print()

def menuConsultar():
    print()

opc = 0
while opc!=6:
    menuPrincipal()
    opc = int(input('Digite uma opção:'))
    if opc == 1:
        menuInserir()
    elif opc==2:
        menuDeletar()
    elif opc==3:
        menuAtualizar()
    elif opc==4:
        menuConsultar()
    elif opc ==5:
        os.system('cls')
        print('Programa Finalizado. ')
    else:
        os.system('cls')
        print('opção invalida. ')
        os.system('pause')
os.system('pause')

    









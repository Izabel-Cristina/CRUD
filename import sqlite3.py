import sqlite3
c = sqlite3.connect('agenda.db')

##conectando com cursor
cursor = c.cursor()

#Caso já exista uma tabela 
cursor.execute("DROP TABLE IF EXISTS AGENDA")

#Criando Tabela
def criar_tabela():
    tabela = """ CREATE TABLE AGENDA1( 
            Nome VARCHAR(30) NOT NULL,
            Email VARCHAR(30) NOT NULL,
            Telefone INTEREGER(14));"""
    cursor.execute(tabela)
    print("Tabela criada com sucesso!")
    

def ler_agenda():
    cursor.execute(""" SELECT*FROM AGENDA1;
    """)
    for linha in cursor.fetchall():
        print(linha)
        
def inserir_dado():
    nome= input("Informe o nome: ")
    email=input("Informe o email: ")
    telefone=int(input("Informe o telefone: "))
    cursor.execute(""" INSERT INTO AGENDA1(nome, email, telefone) VALUES (?,?,?) """,(nome, email, telefone))
    c.commit()
    print('Dados Inseridos com Sucesso!')

def alterar_dado():
    nome= input("Informe o nome: ")
    novo_email =input("Informe o novo email: ")
    novo_telefone = int(input("Informe o  novo telefone: "))
    cursor.execute("""UPDATE AGENDA1 
                    SET email = ?, telefone = ?
                    WHERE nome = ?""", (novo_email, novo_telefone, nome))
    c.commit()
    print('Dados atualizados com sucesso!')
    

def delete_contato():
    nome= input("Informe o nome do contato que deseja excluir: ")
    cursor.execute("""
                    DELETE FROM AGENDA1
                    WHERE nome = ?

                    """, (nome,))
    c.commit()
    print("Contato excluído com sucesso!")
    
print("---------------------AGENDA---------------------")   
print("""
[1] Criar Agenda
[2] Ler Agenda
[3] Inserir Contato
[4] Alterar dados
[5] Excluir Contato
[6] Sair

""")
opc = 0
while opc!=6:
    opc = int(input('Informe a opção desejada: '))
    if opc ==1:
        criar_tabela()
    elif opc ==2:
        ler_agenda()
    elif opc ==3:
        inserir_dado()
    elif opc == 4:
        alterar_dado()
    elif opc == 5:
        delete_contato()
    elif opc == 6:
        print("Finalizado com sucesso")
        c.close
    else:
        print("Opção Invalida!")


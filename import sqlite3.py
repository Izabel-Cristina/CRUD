import sqlite3 
conn = sqlite3.connect('agenda.db')
c = conn.cursor()


def create_tabela():
    c.execute('CREATE TABLE IF NOT EXISTS agenda (Nome TEXTO(30), Telefone TEXTO(14), Email TEXTO(30))')
    print('tabela criada!')
    
def read_tabela():
    c.execute('SELECT * FROM agenda;')
    for linha in c.fetchall():
        print(linha)
    
def alterar_tabela():
    nome_alt = input('Informe o nome: ')
    telefone_alt =input('Informe o telefone: ') 
    email_alt = input('Informe o email: ')
    c.execute('''UPDATE AGENDA
    SET nome = ?, telefone = ?, email = ?''', (nome_alt, telefone_alt, email_alt))
    conn.commit()
    print('Dados atualizados!')



def inserir_dados():
    nome = input('Informe o nome: ')
    telefone =input('Informe o telefone: ') 
    email = input('Informe o email: ')
    c.execute("INSERT INTO agenda(Nome, Telefone, Email) VALUES(?,?,?)", (nome, telefone, email))
    print('Contato salvo com sucesso')

def deletar_dados():
    nome = input('Informe o nome do contato que deseja deletar: ')
    c.execute('''
    DELETE FROM agenda WHERE nome = ?
    ''', (nome)
    )
    print('Contato excluido com sucesso!')

create_tabela()
read_tabela()
alterar_tabela()
inserir_dados()
deletar_dados()



conn.commit()
c.close()
conn.close()

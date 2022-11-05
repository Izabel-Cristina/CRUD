import os
import sqlite3
from sqlite3 import Error

##Conexão
conn = sqlite3.connect('agenda.db')
cursor = conn.cursor()

##Dados do usuário

nome = input('Nome ')
telefone = input('Telefone ')
email = input('Email ')

cursor.execute('''
INSERT INTO agenda (nome, telefone, email)
Values(?,?,?)''', (nome, telefone, email))
conn.commit()

print('Dados Inseridos Com Sucesso! ')

conn.close()


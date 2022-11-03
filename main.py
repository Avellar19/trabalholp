#codigo usado para a vizualizaçao das informaçoes presentes no banco de dados
import sqlite3

conn = sqlite3.connect('empresa.db') 
c = conn.cursor()

v = input('Diga o cpf de quem deseja visualizar os dados: ')

j = c.execute("SELECT * FROM empregados where CPF = '"+v+"'").fetchall()
                     
conn.commit()

print(j)
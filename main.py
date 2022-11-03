import sqlite3

conn = sqlite3.connect('empresa.db') 
c = conn.cursor()

j = c.execute("SELECT * FROM empregados").fetchall()
                     
conn.commit()

print(j)
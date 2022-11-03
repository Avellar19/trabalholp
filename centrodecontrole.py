#chamadas necessarias para utilizar o banco de dados
import sqlite3

conn = sqlite3.connect('empresa.db')
c = conn.cursor()
#fim das chamadas

#definiçao de uma classe que determina as caracteristicas dos funcionarios e exemplifica o funcionamento de orientaçao a objetos em phyton
class funcionarios:
    def __init__(self, CPF, nome, nascimento, setor, cargo, matricula):
        self.CPF= CPF
        self.nome= nome
        self.nascimento= nascimento
        self.setor= setor
        self.cargo= cargo
        self.matricula= matricula
#fim da criaçao da classe

#chamada para definir a açao do usuario
z = int(input("Digite 1 para adicionar funcionario, 2 para remover funcionario, 3 para editar dados de um funcionario ou 4 para visualizar os dados de um funcionario: "))

#primeira açao do usuario: adicionar um funcionario ao banco de dados
if z==1:
    p = input("Me diga seu CPF: ")
    b = input ("Me diga seu nome: ")
    d = input ("Me diga sua data de nascimento: ")
    f = input ("Me diga seu setor: ")
    g = input ("Me diga seu cargo: ")
    h = input ("Me diga sua matricula: ")

    a=funcionarios(''+p+'', ''+b+'', ''+d+'', ''+f+'', ''+g+'', ''+h+'')

    conn = sqlite3.connect('empresa.db') 
    c = conn.cursor()

    c.execute("INSERT INTO empregados VALUES ('"+a.CPF+"','"+a.nome+"','"+a.nascimento+"','"+a.setor+"','"+a.cargo+"','"+a.matricula+"')")
       
                    
    conn.commit()
#fim da açao

#segunda açao do usuario: remover um funcionario do banco de dados
elif z==2:

    conn = sqlite3.connect('empresa.db') 
    c = conn.cursor()

    s = input("Diga o CPF de quem sera excluido: ")

    c.execute("DELETE from empregados where CPF = '"+s+"'")         
                     
    conn.commit()
#fim da açao

#terceira açao do usuario: alterar os dados de um funcionario
elif z==3:

    conn = sqlite3.connect('empresa.db') 
    c = conn.cursor()

    t = input("Me diga o CPF de quem tera os dados alterados: ")
    b = input ("Me diga o novo nome: ")
    d = input ("Me diga a nova data de nascimento: ")
    f = input ("Me diga o novo setor: ")
    g = input ("Me diga o novo cargo: ")
    h = input ("Me diga a nova matricula: ")

    c.execute("update empregados set nome='"+b+"', nascimento='"+d+"', setor='"+f+"', cargo='"+g+"', matricula='"+h+"' where CPF='"+t+"'")
          
                     
    conn.commit()
#fim da açao

#quarta açao do usuario: visualizar os dados de um funcionario
elif z==4:

    conn = sqlite3.connect('empresa.db') 
    c = conn.cursor()
    
    v = input('Diga o cpf de quem deseja visualizar os dados: ')

    j = c.execute("SELECT * FROM empregados where CPF = '"+v+"'").fetchall()
                     
    conn.commit()

    print(j)
#fim da açao
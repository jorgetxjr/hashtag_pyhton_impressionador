import pyodbc
import pprint as pp

dados_conexao = ("Driver={SQLITE3 ODBC Driver};"
                 "Server=localhost;"
                 "Database=salarios.sqlite")
#Se precisar de autenticação, inserir também:
#UID=username
#PWD=senha

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute("SELECT * FROM Salaries")
valores = cursor.fetchall()
pp.pprint(valores[:10])

cursor.close()
conexao.close()
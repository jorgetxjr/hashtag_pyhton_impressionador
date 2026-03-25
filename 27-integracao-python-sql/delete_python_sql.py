import pyodbc

dados_conexao = ("Driver={SQLITE3 ODBC Driver};"
                 "Server=localhost;"
                 "Database=chinook.db")
#Se precisar de autenticação, inserir também:
#UID=username
#PWD=senha

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute('''
DELETE FROM albums WHERE AlgumID =2
               ''')
cursor.commit()


cursor.close()
conexao.close()
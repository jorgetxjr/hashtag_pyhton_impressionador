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
UPDATE customers SET Email= "luisgoncalves@embraer.com"
WHERE Email = "luisg@embraer.com.br"           
''')
cursor.commit()
cursor.execute("SELECT * FROM customers")
tabela = cursor.fetchall()
print(tabela[0])
cursor.close()
conexao.close()
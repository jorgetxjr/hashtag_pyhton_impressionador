import pyodbc
import pprint as pp
import pandas as pd

dados_conexao = ("Driver={SQLITE3 ODBC Driver};"
                 "Server=localhost;"
                 "Database=chinook.db")
#Se precisar de autenticação, inserir também:
#UID=username
#PWD=senha

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute("SELECT * FROM customers")
full_colunas=cursor.description
valores = cursor.fetchall()
colunas=[]
for elemento in full_colunas:
    colunas.append(elemento[0])

print(colunas)
#pp.pprint(valores)
tabela_clientes = pd.DataFrame.from_records(valores, columns=colunas)
print(tabela_clientes)
cursor.close()
conexao.close()
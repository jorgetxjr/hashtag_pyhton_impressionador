import pyodbc
import pprint as pp

dados_conexao = ("Driver={SQLITE3 ODBC Driver};"
                 "Server=localhost;"
                 "Database=chinook.db")
#Se precisar de autenticação, inserir também:
#UID=username
#PWD=senha

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute("""
INSERT INTO albums (Title, ArtistID)
VALUES
('Lira Rock',4)
""")
cursor.commit()

cursor.close()
conexao.close()
import pandas as pd
import sqlite3 as sql

conexao = sql.connect("chinook.db")

LER_CLIENTES = "SELECT * FROM customers"

tabela_clientes = pd.read_sql(LER_CLIENTES,conexao)

print(tabela_clientes)

conexao.close()
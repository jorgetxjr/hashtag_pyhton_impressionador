import pandas as pd
from tqdm import tqdm

produtos_df = pd.read_csv('Contoso - Cadastro Produtos.csv',sep=';',encoding='Latin1')
vendas_df = pd.read_csv('Contoso - Vendas - 2017.csv', sep=';')
lojas_df=pd.read_csv('Contoso - Lojas.csv',sep=';', encoding='Latin1')
clientes_df=pd.read_csv('Contoso - Clientes.csv',sep=';', encoding='Latin1')

clientes_df = clientes_df[['ÿID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'ÿNome do Produto']]
lojas_df = lojas_df[['ÿID Loja', 'Nome da Loja']]

lojas_df=lojas_df.rename(columns={'ÿID Loja':'ID Loja'})
produtos_df = produtos_df.rename(columns={'Nome do Produto':'Nome do Produto'})
clientes_df = clientes_df.rename(columns={'ÿID Cliente':'ID Cliente'})

vendas_df = vendas_df.merge(produtos_df,on="ID Produto")
vendas_df = vendas_df.merge(lojas_df,on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on="ID Cliente")

vendas_df = vendas_df.rename(columns={'E-mail':'E-mail do Cliente'})
vendas_df = vendas_df.rename(columns={"ÿNome do Produto":"Nome do Produto"})

#print(produtos_df)
# print(vendas_df)
# print(lojas_df)
#print(clientes_df)

####Análise de dados
# frequencia_clientes = vendas_df['E-mail do Cliente'].value_counts()
# vendas_por_loja = vendas_df.groupby('Nome da Loja').sum().sort_values('Quantidade Vendida', ascending=False)
# vendas_por_loja = vendas_por_loja['Quantidade Vendida']
# print(vendas_por_loja[:10])

# venda geral
total_vendido = vendas_df['Quantidade Vendida'].sum()
total_devolvido = vendas_df["Quantidade Devolvida"].sum()
print(f"Percentual de devolução geral: {(total_devolvido/total_vendido)*100:.2f}", "%")

# Venda e devolução de uma loja
vendas_europe_online = vendas_df[vendas_df["ID Loja"]==306]
print(vendas_europe_online)
europe_online_total_vendido = vendas_europe_online['Quantidade Vendida'].sum()
europe_online_total_devolvido = vendas_europe_online["Quantidade Devolvida"].sum()
print(f'Percentua de devoução da Europe Online: {(europe_online_total_devolvido/europe_online_total_vendido)*100:.2f}', '%')

#forçando um for, para ver a barra de progresso
progress_bar = tqdm(total=len(vendas_df['ID Loja']),position=0,leave=True)
for i,id_loja in enumerate(vendas_df['ID Loja']):
    if id_loja == 222:
        vendas_df.loc[i,'Quantidade Devolvida']+=1
    progress_bar.update()

print(vendas_df)

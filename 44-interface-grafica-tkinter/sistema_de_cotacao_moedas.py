import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfilename
import pandas as pd
import requests
from datetime import datetime
import numpy as np
import pprint as pp

baseURL ="https://economia.awesomeapi.com.br/json/"

requisicao = requests.get(baseURL+"all")
dicionario_moedas = requisicao.json()

lista_moedas = list(dicionario_moedas.keys())

def pegar_uma_cotacao():
    moeda = combobox_selecionar_moedas.get()
    data_cotacao = calendario_moeda.get()
    ano = data_cotacao[-4:]
    mes =data_cotacao[3:5]
    dia = data_cotacao[:2]
    link = f"daily/{moeda}-BRL/?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}"
    fullLink = baseURL+link
    requisicao_moeda = requests.get(fullLink)
    cotacao = requisicao_moeda.json()
    valor_moeda = float(cotacao[0]['bid'])
    label_resultado_moeda['text'] = f"O fechamento cotação de {moeda} no dia {data_cotacao} foi R${valor_moeda:.2f}."
    

def selecionar_arquivo():
    caminho= askopenfilename(title="selecione o caminho do arquivo de moedas")
    var_caminho_arquivo.set(caminho)
    if caminho:
        label_caminho_arquivo['text'] =f'Arquivo selecionado: {var_caminho_arquivo.get()}'
    

def atualizar_cotacoes():
    try:
        df =pd.read_excel(var_caminho_arquivo.get())
        moedas = df.iloc[:,0]
        data_inicial = calendario_data_inicial.get()
        ano_inicial= data_inicial[-4:]
        mes_incial=data_inicial[3:5]
        dia_inicial=data_inicial[:2]
        data_final = calendario_data_final.get()
        ano_final=data_final[-4:]
        mes_final=data_final[3:5]
        dia_final=data_final[:2]

        for moeda in moedas:
            link = f"daily/{moeda}-BRL/360?start_date={ano_inicial}{mes_incial}{dia_inicial}&end_date={ano_final}{mes_final}{dia_final}" #parece que mudaram a resposta do link, tem que por o número de respostas a ser retornada
            fullLink = baseURL+link
            requisicao_moeda = requests.get(fullLink)
            cotacoes = requisicao_moeda.json()
            for cotacao in cotacoes:
                timestamp_recebido = int(cotacao['timestamp'])
                bid = float(cotacao['bid'])
                data = datetime.fromtimestamp(timestamp_recebido) #lira deu o método errado, mas com ele funcionou.
                data = data.strftime('%d/%m/%Y') #outro vacilo do lira ou atualização da biblioteca?
                                
                if data not in df:
                    df[data] = np.nan
                
                df.loc[df.iloc[:,0] == moeda,data] = bid

        df.to_excel(var_caminho_arquivo.get())
        label_cotacao_atualizada['text'] = "Arquivo atualizado!"
    
    except:
        label_cotacao_atualizada['text'] = "Selecione o arquivo Excel em formato correto"


janela= tk.Tk()
janela.title("Ferramenta de cotação de moedas")

label_cotacao_unica=tk.Label(text="cotação de uma moeda específica", borderwidth=2, relief='solid')
label_cotacao_unica.grid(row=0,column=0,padx=10, pady=10,sticky='nswe', columnspan=3)

label_selecionar_moeda=tk.Label(text="selecione a moeda que quer consultar")
label_selecionar_moeda.grid(row=1,column=0,padx=10, pady=10,sticky='nswe', columnspan=2)

combobox_selecionar_moedas = ttk.Combobox(values=lista_moedas)
combobox_selecionar_moedas.grid(row=1,column=2,padx=10, pady=10,sticky='nswe')

label_selecionar_data =tk.Label(text="Selecione a data que deseja a cotação: ")
label_selecionar_data.grid(row=2, column=0, padx=10, pady=10,sticky='nswe',columnspan=2)

calendario_moeda = DateEntry(year=2026,locale='pt_br')
calendario_moeda.grid(row=2,column=2,padx=10,pady=10,sticky='nswe')

label_resultado_moeda = tk.Label(text="")
label_resultado_moeda.grid(row=3,column=0,padx=10,pady=10,sticky='nswe',columnspan=2)

botao_pegar_cotacao = tk.Button(text="Pegar Cotação", command=pegar_uma_cotacao)
botao_pegar_cotacao.grid(row=3,column=2,padx=10,pady=10,sticky='nswe')


##############################
label_cotacao_multi_moedas=tk.Label(text="cotação de várias moedas", borderwidth=2, relief='solid')
label_cotacao_multi_moedas.grid(row=4,column=0,padx=10, pady=10,sticky='nswe', columnspan=3)
var_caminho_arquivo = tk.StringVar()

label_arquivo = tk.Label(text="Selecione um arquivo em excel com as moedas na coluna A")
label_arquivo.grid(row=5,column=0,columnspan=2,padx=10, pady=10,sticky='nswe')

botao_selecionar_arquivo =tk.Button(text="Selecionar arquivo", command=selecionar_arquivo)
botao_selecionar_arquivo.grid(row=5,column=2,padx=10,pady=10, sticky='nswe')

label_caminho_arquivo = tk.Label(text="Nenhum arquivo selecionado",anchor='e')
label_caminho_arquivo.grid(row=6, column=0,columnspan=3,padx=10,pady=10, sticky='nswe')

label_data_inicial = tk.Label(text="Data inicial")
label_data_inicial.grid(row=7,column=0,padx=10,pady=10,sticky='nswe')

label_data_final = tk.Label(text="Data final")
label_data_final.grid(row=8,column=0,padx=10,pady=10,sticky='nswe')

calendario_data_inicial = DateEntry(year=2026,locale='pt_br')
calendario_data_inicial.grid(row=7,column=1,padx=10,pady=10,sticky='nswe')

calendario_data_final = DateEntry(year=2026,locale='pt_br')
calendario_data_final.grid(row=8,column=1,padx=10,pady=10,sticky='nswe')

botao_atualizar_cotacoes =tk.Button(text="Atualizar cotações",command=atualizar_cotacoes)
botao_atualizar_cotacoes.grid(row=9,column=0,padx=10,pady=10,sticky='nswe')

label_cotacao_atualizada = tk.Label(text="")
label_cotacao_atualizada.grid(row=9,column=1,columnspan=2,padx=10,pady=10,sticky='nswe')

botao_fechar = tk.Button(text="FECHAR",command=janela.quit)
botao_fechar.grid(row=10, column=2, padx=10,pady=10,sticky='nswe')

janela.mainloop()


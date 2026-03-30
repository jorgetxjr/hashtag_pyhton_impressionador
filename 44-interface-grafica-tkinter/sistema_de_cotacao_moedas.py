import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

lista_moedas = ['usd', 'eu']

def pegar_uma_cotacao():
    pass

def selecionar_arquivo():
    pass

def atualizar_cotacoes():
    pass

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


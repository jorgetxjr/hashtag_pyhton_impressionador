import tkinter as tk
from tkinter import ttk

dicionario_cotacoes = {#dummy data
    "Dolar": 5.47,
    "Euro": 6.68,
    "Bitcoin": 20000,
}
lista_moedas = list(dicionario_cotacoes.keys())


def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao.config(text="")
    #mensagem_cotacao.grid(row=3,column=0)
    if cotacao_moeda:
        mensagem_cotacao["text"] = f"Cotação de {moeda_preenchida} é de {cotacao_moeda} reais."
    else:
        mensagem_cotacao["text"] = "Cotação não localizada"


def buscar_cotacoes():
    texto = caixa_texto.get('1.0', tk.END)
    lista_moedas_texto = texto.split('\n') 
    mensagem_cotacoes = []
    for elemento in lista_moedas_texto:
        cotacao = dicionario_cotacoes.get(elemento)
        if cotacao:
            mensagem_cotacoes.append(f'{elemento}:{cotacao}')
    mensagem4 = tk.Label(text='\n'.join(mensagem_cotacoes))
    mensagem4.grid(row=6,column=1)

janela = tk.Tk()
janela.title("Cotação de moedas")

janela.rowconfigure(0,weight=1)
janela.columnconfigure([0,1], weight=1)

mensagem = tk.Label(text="Sistema de busca de cotação de moedas", bg='black',
                    width=32,height=5, fg='white')
mensagem.grid(row=0,column=0, columnspan=2,sticky="Ew")
mensagem2 = tk.Label(text="Selecione a moeda desejada")
mensagem2.grid(row=1,column=0)

# moeda = tk.Entry()
moeda=ttk.Combobox(janela, values=lista_moedas)
moeda.grid(row=1,column=1)


botao = tk.Button(text="Buscar Cotação", command=buscar_cotacao)
botao.grid(row=2,column=1)
mensagem_cotacao = tk.Label(text="")
mensagem_cotacao.grid(row=3,column=0)

mensagem3 = tk.Label(text="caso queira pegar mais de uma cotação, digite as moedas abaixo:")
mensagem3.grid(row=4,column=0, columnspan=2)

caixa_texto = tk.Text(width=10,height=5)
caixa_texto.grid(row=5, column=0,sticky='NSWE')

botao_multicotacoes = botao = tk.Button(text="Buscar Cotações", command=buscar_cotacoes)
botao_multicotacoes.grid(row=5, column=1)


janela.mainloop()
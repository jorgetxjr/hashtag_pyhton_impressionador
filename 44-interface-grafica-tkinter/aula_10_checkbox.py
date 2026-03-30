import tkinter as tk

janela = tk.Tk()

def enviar():
    if var_promcoes.get():
        print("receberá promoções")
    else:
        print("não receberá promoções")


var_promcoes = tk.IntVar()
check_promocoes =tk.Checkbutton(text="deseja receber e-mails promocionais?", variable=var_promcoes)
check_promocoes.grid(row=0, column=0)

var_politicas = tk.IntVar()
check_politicas = tk.Checkbutton(text="Aceita as nossas poíticas de contrato?", variable=var_politicas)
check_politicas.grid(row=1,column=0)

botao_enviar = tk.Button(text="ENVIAR", command=enviar)
botao_enviar.grid(row=2,column=0)

janela.mainloop()
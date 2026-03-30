import tkinter as tk

janela = tk.Tk()

def enviar():
    print(var_class.get())

var_class = tk.StringVar(value="não consigo ler nada")
bt_classe_economica = tk.Radiobutton(text="Classe Econômica",variable=var_class, value='Classe Econômica')
bt_classe_executiva = tk.Radiobutton(text="Classe Executiva",variable=var_class, value='Classe Executiva')
bt_primeira_class = tk.Radiobutton(text="Primeira Classe",variable=var_class, value='Primeira Classe')
bt_classe_economica.grid(row=0,column=0)
bt_classe_executiva.grid(row=0,column=1)
bt_primeira_class.grid(row=0, column=2)

botao_enviar = tk.Button(text='ENVIAR', command=enviar)
botao_enviar.grid(row=1,column=1)
janela.mainloop()
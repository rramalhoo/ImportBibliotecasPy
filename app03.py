import tkinter as tk

janela = tk.Tk()
janela.title("meu app")
janela.geometry("300x200")

botao = tk.Button(janela, text= "clique aqui")
botao.pack(pady=0)

janela.mainloop()
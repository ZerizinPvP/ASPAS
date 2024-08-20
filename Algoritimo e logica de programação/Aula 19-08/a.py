import tkinter as tk
from tkinter import ttk

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo de Treeview")

# Criação do widget Treeview
tree = ttk.Treeview(root)

# Definição das colunas
tree['columns'] = ('Nome', 'Idade', 'Profissão')

# Formatação das colunas
tree.column("#0", width=120, minwidth=25)
tree.column("Nome", anchor=tk.W, width=120)
tree.column("Idade", anchor=tk.CENTER, width=80)
tree.column("Profissão", anchor=tk.W, width=120)

# Definição dos cabeçalhos
tree.heading("#0", text="ID", anchor=tk.W)
tree.heading("Nome", text="Nome", anchor=tk.W)
tree.heading("Idade", text="Idade", anchor=tk.CENTER)
tree.heading("Profissão", text="Profissão", anchor=tk.W)

# Adicionando dados
tree.insert(parent='', index='end', iid=0, text='1', values=('Ana', 30, 'Engenheira'))
tree.insert(parent='', index='end', iid=1, text='2', values=('Bruno', 25, 'Programador'))
tree.insert(parent='', index='end', iid=2, text='3', values=('Carlos', 35, 'Designer'))

# Posicionando o Treeview na janela
tree.pack(pady=20)

# Executando a janela
root.mainloop()

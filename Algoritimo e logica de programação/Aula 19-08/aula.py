import tkinter as tk

# Função para capturar e armazenar os nomes
def capturar_nome():
    nome = entry_nome.get()
    if nome and len(nomes) < 5:  # Verifica se o campo não está vazio e se ainda não há 5 nomes
        nomes.append(nome)
        entry_nome.delete(0, tk.END)  # Limpa o campo de entrada
        if len(nomes) == 5:
            exibir_nomes()

# Função para exibir os nomes na interface
def exibir_nomes():
    for i, nome in enumerate(nomes):
        label_nome = tk.Label(app, text=nome)
        label_nome.place(x=20, y=120 + i*20)

# Configurações da janela principal
app = tk.Tk()
app.title("Captura de Nomes")
app.geometry("300x250")

# Lista para armazenar os nomes
nomes = []

# Campo de entrada para o nome
Ib_1 = Label(frame, text="Contatos:", fg='red', font=("Arial", 14, "bold italic"))
Ib_1.grid(row=0, column=0, padx=10, pady=10)
label_instrucao = tk.Label(app, text="Digite um nome:")
label_instrucao.place(x=20, y=20)
entry_nome = tk.Entry(app)
entry_nome.place(x=20, y=50)

# Botão para capturar o nome
botao_capturar = tk.Button(app, text="Capturar Nome", command=capturar_nome)
botao_capturar.place(x=20, y=80)

# Inicia o loop principal da aplicação
app.mainloop()
"""from tkinter import *

# Definindo a função capturar ao clicar no botão
def capturar():
    Ib_3['text'] = nome.get()

# Criando a aplicação
app = Tk()
app.title('Análise e Desenvolvimento de Sistemas')
app.geometry('1360x688')  # largura e altura
app.configure(background='#F8F8FF')
app.resizable(True, True)
app.minsize(width=1360, height=670)
app.maxsize(width=1360, height=670)

# Adicionando um Frame LabelFrame
frame = LabelFrame(app, text="Cadastro", borderwidth=1, relief='solid')
frame.place(x=10, y=10, width=1340, height=340)

# Inserindo e posicionando um Label dentro do frame
Ib_1 = Label(frame, text="Contatos:", fg='red', font=("Arial", 12, "bold italic"))
Ib_1.place(x=15, y=10, width=80, height=20)
Ib_2 = Label(frame, text='Digite um nome:', font=("Arial", 12))
Ib_2.place(x=20, y=35, width=120, height=20)

# Inserindo e posicionando um Entry dentro do frame
nome = Entry(frame, font=('Arial', 14))
nome.place(x=135, y=35, width=400, height=20)

# Definindo o foco no campo "nome"
nome.focus_set()

# Definindo a label que irá capturar os dados digitados ao clicar no botão
Ib_3 = Label(app, text="", font=("Arial", 14), background="#F8F8FF")
Ib_3.place(x=135, y=370, width=400, height=20)

# Implementando um botão
btn_captura = Button(app, text="Capturar dados", font=("Arial", 12, "bold"), command=capturar)
btn_captura.place(x=490, y=300, width=125, height=40)

# Iniciando o loop da aplicação
app.mainloop()
"""

from tkinter import *

# Função para adicionar o nome à lista e atualizar a exibição
def adicionar_nome():
    nome_digitado = nome.get().strip()  # Remove espaços extras
    if nome_digitado:
        if len(nomes) < 5:  # Verifica se ainda há espaço na lista
            nomes.append(nome_digitado)
            atualizar_exibicao()
            nome.delete(0, END)  # Limpa o campo de entrada
            if len(nomes) == 5:  # Se todos os nomes foram inseridos
                btn_adicionar.config(state=DISABLED)  # Desabilita o botão
        else:
            Ib_3.config(text="Você já inseriu 5 nomes.")
    else:
        Ib_3.config(text="O campo de entrada está vazio.")

# Função para atualizar a exibição dos nomes na tela
def atualizar_exibicao():
    exibir_texto = "\n".join(nomes)
    Ib_4.config(text=exibir_texto)

# Criando a aplicação
app = Tk()
app.title('Análise e Desenvolvimento de Sistemas')
app.geometry('500x400')  # Ajustando a largura e altura para melhor visualização
app.configure(background='#F8F8FF')
app.resizable(False, False)

# Lista para armazenar os nomes
nomes = []

# Adicionando um Frame LabelFrame
frame = LabelFrame(app, text="Cadastro", borderwidth=1, relief='solid')
frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Inserindo e posicionando Labels e Entry dentro do frame
Ib_1 = Label(frame, text="Contatos:", fg='red', font=("Arial", 14, "bold italic"))
Ib_1.grid(row=0, column=0, padx=10, pady=10)

Ib_2 = Label(frame, text='Digite um nome:', font=("Arial", 14))
Ib_2.grid(row=1, column=0, padx=10, pady=10)

nome = Entry(frame, font=('Arial', 14))
nome.grid(row=1, column=1, padx=10, pady=10, sticky=W+E)
nome.focus_set()

# Definindo a label que irá capturar e mostrar mensagens
Ib_3 = Label(app, text="", font=("Arial", 14), background="#F8F8FF")
Ib_3.pack(pady=10)

# Definindo a label para exibir os nomes
Ib_4 = Label(app, text="", font=("Arial", 14), background="#F8F8FF", justify=LEFT)
Ib_4.pack(pady=10, padx=10, fill=BOTH, expand=True)

# Implementando um botão para adicionar nomes
btn_adicionar = button(app, text="Adicionar Nome", font=("Arial", 14, "bold"), command=adicionar_nome)
btn_adicionar.pack(pady=10)

# Iniciando o loop da aplicação
app.mainloop()

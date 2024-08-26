from tkinter import *

# Função para capturar o nome do primeiro botão
def capturar():
    Ib_3['text'] = nome.get()

# Função para capturar e armazenar os nomes no segundo conjunto
def capturar_nome():
    nome_digitado = entry_nome.get()
    if nome_digitado and len(nomes) < 5:  # Verifica se o campo não está vazio e se ainda não há 5 nomes
        nomes.append(nome_digitado)
        entry_nome.delete(0, END)  # Limpa o campo de entrada
        if len(nomes) == 5:
            exibir_nomes()

# Função para exibir os nomes na interface
def exibir_nomes():
    for i, nome in enumerate(nomes):
        label_nome = Label(frame_captura, text=nome)
        label_nome.place(x=20, y=120 + i*20)

# Criando a aplicação
app = Tk()
app.title('Análise e Desenvolvimento de Sistemas')
app.geometry('1360x688')  # Largura e altura
app.configure(background='#F8F8FF')
app.resizable(True, True)
app.minsize(width=1360, height=670)
app.maxsize(width=1360, height=670)

# Adicionando um Frame LabelFrame para o primeiro conjunto
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

# Implementando um botão para o primeiro conjunto
btn_captura = Button(app, text="Capturar dados", font=("Arial", 12, "bold"), command=capturar)
btn_captura.place(x=490, y=300, width=125, height=40)

# Frame para a segunda funcionalidade de captura de nomes
frame_captura = LabelFrame(app, text="Contato", borderwidth=1, relief='solid')
frame_captura.place(x=10, y=400, width=1340, height=250)

# Label e Entry para o segundo conjunto
label_instrucao = Label(frame_captura, text="Digite um nome:", font=("Arial", 12))
label_instrucao.place(x=20, y=20)
entry_nome = Entry(frame_captura, font=('Arial', 14))
entry_nome.place(x=20, y=50, width=400, height=20)

# Botão para capturar o nome no segundo conjunto
botao_capturar = Button(frame_captura, text="Capturar Nome", font=("Arial", 12, "bold"), command=capturar_nome)
botao_capturar.place(x=440, y=45, width=125, height=40)

# Lista para armazenar os nomes
nomes = []

# Iniciando o loop da aplicação
app.mainloop()

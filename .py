import tkinter as tk

# Lista para armazenar os produtos
carrinho_de_compras = []

# Função para adicionar um produto ao carrinho
def adicionar_produto():
    id_produto = entry_id.get()
    descricao = entry_descricao.get()
    quantidade = entry_quantidade.get()
    preco = entry_preco.get()

    # Verifica se todos os campos foram preenchidos
    if id_produto != "" and descricao != "" and quantidade != "" and preco != "":
        produto = {
            'id': id_produto,
            'descricao': descricao,
            'quantidade': quantidade,
            'preco': preco
        }
        carrinho_de_compras.append(produto)
        # Limpa os campos após adicionar o produto
        entry_id.delete(0, tk.END)
        entry_descricao.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)
        entry_preco.delete(0, tk.END)

# Função para exibir os produtos cadastrados
def exibir_produtos():
    janela_produtos = tk.Toplevel()
    janela_produtos.title("Produtos cadastrados")
    
    for produto in carrinho_de_compras:
        texto = f"ID: {produto['id']}, Descrição: {produto['descricao']}, Quantidade: {produto['quantidade']}, Preço: R${produto['preco']}"
        label_produto = tk.Label(janela_produtos, text=texto)
        label_produto.pack()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Cadastro de Produtos")

# Criando labels e entradas para os dados do produto
label_id = tk.Label(janela, text="ID do Produto:")
label_id.grid(row=0, column=0, padx=10, pady=10)
entry_id = tk.Entry(janela)
entry_id.grid(row=0, column=1, padx=10, pady=10)

label_descricao = tk.Label(janela, text="Descrição do Produto:")
label_descricao.grid(row=1, column=0, padx=10, pady=10)
entry_descricao = tk.Entry(janela)
entry_descricao.grid(row=1, column=1, padx=10, pady=10)

label_quantidade = tk.Label(janela, text="Quantidade:")
label_quantidade.grid(row=2, column=0, padx=10, pady=10)
entry_quantidade = tk.Entry(janela)
entry_quantidade.grid(row=2, column=1, padx=10, pady=10)

label_preco = tk.Label(janela, text="Preço:")
label_preco.grid(row=3, column=0, padx=10, pady=10)
entry_preco = tk.Entry(janela)
entry_preco.grid(row=3, column=1, padx=10, pady=10)

# Botão para adicionar o produto
btn_adicionar = tk.Button(janela, text="Adicionar Produto", command=adicionar_produto)
btn_adicionar.grid(row=4, column=0, columnspan=2, pady=10)

# Botão para exibir os produtos cadastrados
btn_exibir = tk.Button(janela, text="Exibir Produtos", command=exibir_produtos)
btn_exibir.grid(row=5, column=0, columnspan=2, pady=10)

# Executando a janela principal
janela.mainloop()

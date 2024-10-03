def app():
    global soma, pares, impares
    numeros = []
    print("Digite 9 números inteiros: ")

    while len(numeros) < 9:
        try:
            num = int(input(f"Digite o {len(numeros) + 1}° número: "))
            numeros.append(num)
        except ValueError:  # Captura apenas erros de conversão para int
            print('Erro: Por favor, digite um número inteiro.')

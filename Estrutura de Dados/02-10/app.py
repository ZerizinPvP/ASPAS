def app():
    global soma , pares , impares
    numeros = []
    print("Digite 9 números inteiros: ")

    for i in range(9):
        try: 
            num = int(input(f"Digite o {i + 1}° numero: "))
            numeros.append(num)
            soma = sum(numeros)
            pares = [num for num in numeros if num % 2 == 0]
            impares = [num for num in numeros if num % 2 != 0]
        except:
            print('Erro, execute o programa novamente')
            continue
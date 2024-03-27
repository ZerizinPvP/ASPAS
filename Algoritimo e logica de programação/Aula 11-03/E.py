"""
João vitor Gomes Zeri
script1.py UTF8 - PT-BR
Data: 25-03-2024
"""
#Exercicio E

Valor_Salario = float(input('Qual o valor do teu salario ? R$: '))

print(f'\n O salario atual é de : {Valor_Salario}')

Valor_Salario *= 1.45

print(f'\nO novo salrio é de: {Valor_Salario}')

if Valor_Salario < 2000:
    print(f'\nVocê tera aumenteo dessa vez...')
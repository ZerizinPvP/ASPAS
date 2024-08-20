"""
João vitor Gomes Zeri
script1.py UTF8 - PT-BR
Data: 25-03-2024

#Exercicio A

carro = int(input('Quantos anos tem seu carro ? '))
if carro > 2:
    print(f'Seu carro esta ficando velho, ele tem {carro} anos ')
    
    
#Exercicio B

    velocidade = int(input('quantos Km/h teu carro consegue de final ?: '))
if velocidade > 80:
    print(f'se andar nessa velocidade de {velocidade} km/h vai tomar multa. ')
    
#Exercicio C

Valor_Medio_Anual = float(input('Valor medio anual : R$'))

if Valor_Medio_Anual <= 19038.00:

    print(f'Sua aliquota de imposto para o ano de 2024 sera de 0%')
    
    
#Exercicio D

valor_1 = float(input('\nDigite o 1° Valor ? '))

valor_2 = float(input('\nDigite o 2° Valor ? '))

if valor_1 > valor_2:
    print(f'\nO primeiro numero é maior {valor_1}')
    
if valor_2 > valor_1:
    print(f'\nO segundo valor é maior: {valor_2}')


#Exercicio E

Valor_Salario = float(input('Qual o valor do teu salario ? R$: '))

print(f'\n O salario atual é de : {Valor_Salario}')

Valor_Salario *= 1.45

print(f'\nO novo salrio é de: {Valor_Salario}')

if Valor_Salario < 2000:
    print(f'\nVocê tera aumenteo dessa vez...')
  
    
#Exercicio F

carro = int(input('Quantos anos tem seu carro ? '))
if carro <= 2:
    print(f'Seu carro esta novo, ele tem {carro} anos ')
else:
    print(f'Seu carro esta ficando velho, ele tem {carro} anos ')


#Exercicio G

velocidade = int(input('quantos Km/h teu carro consegue de final ?: '))

velocidade1 = int(input('qual velocidade maxima você costuma andar ?: '))

if velocidade1 > 80:
    print(f'se andar nessa velocidade de {velocidade1} km/h vai tomar multa. ')
else:
    print('Parabens você é um motorista prudente')
    
#Exercicoo H

Valor_Medio_Anual = float(input('qual teu rendimento medio anual: R$ '))

if Valor_Medio_Anual <= 1903.98:
    print(f'Sua aliquota de imposto para o ano de 2024 sera de 0%')
else:
    print(f'Sua aliquota de imposto para o ano de 2024 sera de 7,5%')
    
    """
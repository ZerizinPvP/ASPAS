#João Vitor Zeri 09-09
"""
try: #tente fazer isso 
    nota_1 = float(input('Digite a 1° nota: '))
    nota_2 = float(input('Digite a 2° nota: '))
    nota_3 = float(input('Digite a 3° nota: '))
    nota_4 = float(input('Digite a 4° nota: '))
    print()
    print(f'A soma das quatro notas é : {nota_1+nota_2+nota_3+nota_4}')
    print()
    print(f'A media das quatro notas é : {(nota_1+nota_2+nota_3+nota_4)/4}')
except ValueError: #apresenta a mensagem caso der erro
    print('Digite apenas numeros: ')
finally:
    print('Bloco finalizado')

try: #tente fazer isso 
    nota_1 = float(input('Digite a 1° nota: '))
    nota_2 = float(input('Digite a 2° nota: '))
    nota_3 = float(input('Digite a 3° nota: '))
    nota_4 = float(input('Digite a 4° nota: '))
    print()
    media = ((nota_1+nota_2+nota_3+nota_4)/4)
    print()
    print(f'A media das quatro notas é : {(nota_1+nota_2+nota_3+nota_4)/4}')
    print()
#print(fA média das quatro notas é: (media}')
    if media >= 60:
        print(f'Aprovado com média: {media}') 
    elif media < 60 and media >= 40:
        print('Exame média: {media}')
    elif media < 40 and media >30:
        print(f'Só o conselho para ajudar - média: {media}')
    else:
        print(f'Retido na disciplina - média: {media}')
except ValueError: # apresente a mensagem abaixo se ocorrer um erro
    print('Digite apenas números: ')
finally:
    pass
--
B)
nome = ""
try:
    nome = input('Digite seu nome: ')

    if nome.isalpha and len(str(nome))>=1: 
        for letra in nome: print(f'A letra do nome digitado foi: {letra}') 
except ValueError: 
    print(f'\nDigite apenas caracteres')
finally:
    pass
--   
C)
try:
    disciplina = input('Digite o nome da disciplina: ')

    if not disciplina.isalpha(): 
        print('Digite apenas caracteres')
    else:
        for indice, letra in enumerate(disciplina): 
            if (indice % 2) != 0: print(f'{indice}: {letra}')
except Exception as e: 
    print(f'Uma exceção ocorreu: {e}')
finally:
    pass
--
D)
try:
    nome_curso = input('Digite o nome do Curso disciplina: ')
    print()
    if nome_curso.isalpha and len(str(nome_curso))>0:
        
        for indice_letra in enumerate(nome_curso):
        
            if ((indice_letra[1].upper())) in 'AEIOU':
                print(indice_letra[1].upper())
except ValueError:
    print('Digite apenas caracteres')
finally:
    pass
--
E)
try:
    cidade_nasceu = input('Digite o nome da cidade onde nasceu: ')
    print()
    if cidade_nasceu.isalpha():
        for letra in cidade_nasceu: 
            if letra.upper() in 'BCDFGHJKLMNPQRSTVXWZÇ': print(letra.upper())
    else:
        print('Digite apenas caracteres')
except Exception as e:
    print(f'Ocorreu um erro: {e}')
finally:
    pass
    
import time
    
for tabela in range(32, 124): 
         print(f'O código da tabela ASC é: {tabela} - que corresponde = {chr(tabela)}') 
time.sleep(0.0005)
--
F)
import time
nr = 0
for i in range(8):
    print(f'Indices: {i}')
    nr +=1
    time.sleep(0.0005)
print(f'\no total de índices mostrados na tela é: {nr} \n')

G)
try:
    indice_inicial = int(input('Digite o indice inicial: '))
    indice_final = int(input('Digite o indice final...:'))
    print()
    if indice_inicial < 0:
        print(f'O indice inicial: {indice_inicial} não pode ser menor que 0-programa encerrado.')
    elif indice_final <= indice_inicial:
        print(f'O indice inicial: {indice_inicial} não pode ser maior ou igual ao indice final: {indice_final} - programa encerrado.')
    else:
        for i in range (indice_inicial, indice_final):
            print(f'indice {i}')
        print(f'fino total de índices mostrados na tela é: {indice_final-indice_inicial} \n')
except ValueError:
    print('\nDigite apenas números inteiros... \n')

try:
    nr = 0
    indice_inicial = int(input('Digite o indice inicial: '))
    indice_final = int(input('Digite o indice final....'))
    print()
    
# Critério H: O número indice inicial não pode ser menor que zero nem maior ou igual ao número do indice final 
    if indice_inicial <0 or indice_inicial >= indice_final:
        print(f'O indice inicial: {indice_inicial} não pode ser menor que zero ou maior ou igual ao indice final: {indice_final} - programa encerrado') 
    else:
        numeros_ignorados = [] # uma lista para armazenar os números a serem ignorados 
        #Critério J: Permitir que o usuário possa definir 3 números que deverão ser ignorados 
        while len(numeros_ignorados) <3: # peça ao usuário para inserir 3 números para ignorar 
            numero_ignorado = int(input('Digite um número para ignorar: '))
            if numero_ignorado not in numeros_ignorados: numeros_ignorados.append(numero_ignorado)
        else:
            print('Esse número já foi escolhido para ser ignorado, escolha outro número.')
    for i in range(indice_inicial, indice_final, 5):
        if i not in numeros_ignorados: # só imprima o número se ele não estiver na lista de números ignorados 
            print(f'indice: (i)') 
            nr += 1
            
        #Critério I: Deve ser apresentado no mínimo 4 elementos na tela
        if nr < 4: 
            print(f'Quantidade de indices incompatível com os critérios pedidos no script: pedidos = 4, intervalo tem apenas: {nr}')
        else:
            print(f'O total de indices mostrados na tela é: {nr}')
except ValueError:
    print('Digite apenas números inteiros...')
    
globals()

num = 42

print(f'\nA variavel num:{num} é do tipo :{type(num)}')
print(f'\nO endereço de memoria da variavel num é :{id(num)}')
print(f'\nvariaveis globais do módulo:{goblais()}')

num = 'Curso de ADS'

print(f'\nA variavel num:{num} é do tipo :{type(num)}')
print(f'\nO endereço de memoria da variavel num é :{id(num)}')
print(f'\nvariaveis globais do módulo:{goblais()}\n')

if True:
    variavel_local = 10
    print(f'ino valor da variavel_local é dentro do if é: {variavel_local} \n')

print(f'O valor da variável_local fora do bloco if é: {variavel_local}')

variavel_local += 50

for i in range(2):
    variavel_local += 30
    print(f'\no valor da variavel_local dentro do for é: {variavel_local}')
    break

variavel_local += 5

while True:
    variavel_local += 5
    print(f'\no valor da variavel_local dentro do while é: {variavel_local} \n')
    break

variavel_local +=5

print(f'O valor da variável_local fora do bloco while é: {variavel_local} \n')

#Imprimindo uma string com For em uma linha

disciplina = 'Algoritmo e lógica de programação'
for nome in disciplina:
    print(nome, end = '')

# Imprimindo uma mesma string com for várias vezes:
for numero in range(1,9): 
    print('ADS '* numero)


# - Função de soma
def soma(valor_1, valor_2):
    print(valor_1 + valor_2)

# - chamando uma função criada
soma(25, 100)

# - Função que faz o cálculo para par ou ímpar
def parlmpar(numero): return numero % 2 == 0

def par_ou_impar(numero):
    if parlmpar(numero) == True:
        return 'par'
    else:
        return 'impar'
"""
"""
print(par_ou_impar(123))
print(par_ou_impar(48))

"""
"""

def pesquisa(lista, valor_a_pesquisar):
    try:
        return lista.index(valor_a_pesquisar)
    except ValueError:
        return None

lista_1= [51, 25, 2021, 2022, 'IFRO']

print(pesquisa(lista_1, 2022))
print(pesquisa(lista_1, 'IFRO'))

print('Imprimindo o argumento passado')

indice = pesquisa(lista_1, 51)
if indice is not None:
    print(lista_1[indice])
else:
    print("Elemento não encontrado na lista.")

"""
"""
empresa = 'dias e Dias Parados'
def imp_cabecalho():
    print(empresa)

imp_cabecalho()

"""
"""
from random import random

def joga_moeda():
    valor = random()
    if valor> 0.5:
        return'Cara'
    else:
        return'Coroa'
    print(joga_moeda())
"""
"""
def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, mensagem)
    return(num1 + b) * mensagem

print(multiplica(4,5))
print(outra(2,5,'IFRO'))
"""
"""
def nome_completo(nome, sobrenome):
    return f'Seu nome é {nome} {sobrenome}'

print(nome_completo('Claudinei','de Oliveira'))

"""
"""
print(nome_completo(nome = 'Gertrudezi', sobrenome='de Gomes Pascoal'))

"""
"""
print('IFRO Campus Ariquemes')


"""
"""
Def quadrado(numero):
    return numero **2

print(quadrado(5))

"""
"""
def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencial(4,3))
print(exponencial(2))
"""
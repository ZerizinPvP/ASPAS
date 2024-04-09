"""
Exercicio A Concatenando variáveis
instituição = 'Instituto '
esfera = 'Federal '
print(f'\nO nome da instituição é: {instituição + esfera} \n')
"""

"""
Exercicio B Fatiando String
instituicao = 'Instituto Federal de Rondônia '
print(f'\nApresentando os 10 primeiros caracters da sting: {instituicao[:10]} \n')
"""

""" 
Exercicio C Fatiando string - apresentando um recorte
instituicao = 'Instituto Federal de Rondônia '
print(f'\nApresentando dados 5° ao 15° caracters da sting: {instituicao[5:25]} \n')
"""

"""
Exercicio D Fatiando String - apresentando um recorte pulando e caracteres
instituicao = 'Instituto Federal de Rondônia '
print(f'\nApresentando dados do indice 0° ao 20°, pulando de 3 em 3 caracteres: {instituicao[0:20:3]}: \n')
"""
"""
#E) Fatiando Strings - substituindo o primeiro caractere:
nome = 'Astrogildo'
nome = 'O' + nome[1:]
print(f'\nO novo nome é: {nome} \n')"""


"""
f) Fatiando Strings - invertendo os caracteres da string

disciplina = 'Algoritimo e logica de programação'
print(f'\nA palavra intertida é: {disciplina[::-1]}\n')
"""

"""
g) Fatiando Strings - substituindo caracteres
palavra = 'paralelepipedo'
palavra = palavra.replace('l','r')
print(f'\nA palavra tocando a letra L por R = {palavra}\n')
"""
"""
h) Fatiando Strings - dados a partir do índice 3 e finaliza 5 índices antes do final

palavra = 'reconstituicionalissimamentemente'
palavra = palavra[2 : -5]
print(f'\nA palavra que recebei dados a partir do indice 3 e ate o indice 5 = {palavra}\n')
"""

"""
i)Verificando o caractere que inicia a palavra - startswith()

palavra = 'Desenvolvimento'
print(f'\nPalavra escoclida: {palavra}')
print(f'\nA palavra inicia com a letra D ? {palavra.startswith("D")}')
print(f'\nA palavra inicia com a letra J ? {palavra.startswith("j")}\n')
"""

"""
J)Verificando o caractere do final da palavra - endswith()
palavra = 'Inovação'
print(f'\nPalavra escoclida: {palavra}')
print(f'\nA palavra inicia com a letra M ? {palavra.endswith("D")}')
print(f'\nA palavra inicia com a letra o ? {palavra.endswith("j")}\n')
"""

"""
k) Verificando o caractere do início e final da palavra -startswith() e endswith()

palavra = 'Oportunidade'
print(f'\nPalavra escoclida: {palavra}')
print(f'\nA palavra inicia com a letra D ? {palavra.startswith("D")} - e termina com a letra e ? {palavra.endswith("e")}\n')
"""

"""
L) ASC = obtendo o código da tecla ou letra do código


print('\n' 'a' > 'x')
print(f'\nO valor de "a" na tabela asc é chr(97):{chr(97)}')
print(f'\nO valor de "X" na tabela asc é chr(88):{chr(88)}')

print(f'\nO valor de "a" extraido da função ord():{ord("a")}')
print(f'\nO valor de "X" extraido da função ord():{ord("X")}')
"""

"""
#M)
i = 0
nome = input('Insira teu nome completo:\n')
nome2 = ''
control = False

while i < len(nome):
    if nome[i].isalpha()is True:
        nome2 += nome[i]
        control = False
    elif nome[i].isalpha() is False and control is False:
        nome2 += ' '
        control = True
        nome3 = nome2.upper()
    i += 1
print(nome3)
"""


"""

n) for() para apresentar os valores de uma variável iterável

ifro = 'Ariquemes'
for letra in ifro:
    print(letra)
"""
"""
o) for() para apresentar os valores de uma variável iterável nas mesma linha.

ifro = 'Ariquemes'
for letra in ifro:
    print(letra, end='')
"""

"""
p) for() + enumerate() - apresenta o índice e valor de cada índice da variável

ifro = 'Campus Ariquemes'
for indice_letra in enumerate(ifro):
    print(indice_letra)
print()

Interpretando a estrutura acima: para cada letra dentro do iterável campus
imprima o índice e a letra
"""
"""
q) for() + enumerate - apresenta apenas o índice de cada letra da variável

ifro = 'Campus Ariquemes'
for indice_letra in enumerate(ifro):
    print(indice_letra[0])
print()
"""
"""
r) for() + enumerate - acessando apenas os valores do iterável

ifro = 'Campus '
for indice_letra in enumerate(ifro):
    print(indice_letra[1])
print()

"""

"""
s)Desenvolva um script com for() que mostra na tela os os números de 0 a 9

for x in range(10):
    print(x)
print()
"""
"""
t) Desenvolva um script com for que mostra os números de 0 a 9 - decrescente

for i in range(10,0,-1):
    print(i)
print()
"""
"""
u) - break para interromper a estrutura de repetição:

for i in range(10):
    if i == 5:
        break
    else:
        print(i)
print()
"""

"""
v) for(), range e else para imprimir i enquanto este for menor ou igual a 3
for i in range(3):
    if i == 5:
        print (f'\nO range ultrapassou os limites...')
    print(f'\n O valor de i é: {i}')
else:
    print(f'\nFor() executado com sucesso, valor de i é {i} \n')
"""
"""
x) aplicando for(), range(), if e continue onde precisamos imprimir ou realizar
algum cálculo somente com números ímpares. 


for i in range(20):

    if(i%2 == 0):
        continue
    print(i)
"""


#z)exercicio 
limi_cap = 5

for i in range(0, limi_cap + 1):
    if i == limi_cap:
        print("A sala alcançou sua capacidade máxima.")
        break
    else:
        print(f"Pessoa número {i} entrou na sala.")
print("Capacidade máxima da sala atingida.")

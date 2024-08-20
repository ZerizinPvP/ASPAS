"""
João vitor Gomes Zeri
script1.py UTF8 - PT-BR
Data: 25-03-2024

#Exercicio A
media = float(input('\nDigite a media do aluno(a):'))

if media >= 60: #se a media é maior ou igual a 60
    print('\nAprovado\n') #verdadeiro - "aprovado"
    
elif 40 < media < 60: #se a media esta entre 40 e 60
    print('\nRecuperação\n') #se for entre esse valor ele vai colocar "aprovado"
    
elif 20 < media <= 40: #se a meida esta entre 20 e 40 
    print('\nExame\n') #ele vai colocar como "exame"

else:#se nenhuma das contiçoes estiverem no padrao colocado ele estara reprovado.
    print('\nReprovado\n')


#Exercicio B

n1 = int(input('Digite o primeiro numero inteiro: ')) #pede o primeiro numero

n2 = int(input('Digite o segundo numero inteiro: ')) #pede o segundo numero

n3 = int(input('Digite o terceiro numero inteiro: ')) #pede o terceiro numero

if n1 > n2 and n1 > n3:#verifica se o primeiro numero é o maior
    print(f'\nO maior numero digitado foi {n1}')
    
elif n2 > n1 and n2 > n3:#verifica se o segundo numero é o maior
    print(f'\nO maior numero digitado foi {n2}')
    
else:#verifica se o terceiro numero é o maior
    print(f'\nO maior numero digitado foi {n3}')



#Exercicio C

N = int(input('Digite um numero INTEIRO podendo ele ser negativo ou positivo: '))

if N >= 0 :
    print(f'\nO numero {N} é Positivo')
else:
    print(f'\nO numero {N} é Negativo')
    


#Exercicio D

tempo_fa = float(input('Digite a temperatura em Fahrenheit: '))
tempo_ce = 5 * ((tempo_fa - 32) / 9)

if tempo_ce >= 26:
    print(f'{tempo_ce:.2f}°c\nEsta muito calor, melhor se proteger')
    
elif 18 <= tempo_ce < 26:
    print(f'{tempo_ce:.2f}°c\nClima esta agradavel, que tal um passeio')
    
else:
    print(f'{tempo_ce:.2f}°c\nEsta ficando frio melhor se agasalhar')



#Exercicio E

preco = 0 # define variável do preço

if tipo == 'R': # verifica se é Residencial
    if consumo <= 700:
        preco = 0.42
    else:
        preco = 0.50

elif tipo == 'C': # verifica se é comercial
    if consumo <= 1400:
        preco = 0.55
    else:
        preco = 0.65

elif tipo == 'I': # Verifica se é industrial
    if consumo <= 5100:
        preco = 0.58
    else:
        preco = 0.69

else: # se tipo de instalação não seja reconhecida
    preco = 0
    print(f'\nErro!!! tipo de instalação desconhecida... \n')

if preco > 0: # verifica se o preço é maior que 0
    custo = consumo * preco
    print(f'\nO tipo de instalação é {tipo} e o valor a pagar é de: R$ {custo:.2f}\n')

else: # se preço = zero, não calcula o custo e apresenta mensagem
    print(f'\nNão foi possível calcular o custo devido ao tipo de instalação desconhecido. \n')



#Exercico F

n = 1 # define n com 1 
while n <= 100: # enquanto N for menor ou igual a 100 vai repetir os numeros
    print(n) # imprime o valor de N
    n += 1 #soma +1 ate chegar no 100



#Exercicio G

n = 9
while n >= 0: #enquanto o N for menor que 0
    print(f'\nFaltam {n} Segundos para o lançamento')
    n -= 1 # sempre que voltar aqui ele vai subitrair 1



#Exercicio H

numero = int(input('\nDigite o Ultimo numero que será apresentado na tela: '))

n = 1 #inicializando o contador

while n <= numero: #enquanto o numero digitado pelo usuario for menor que N vai ficar no loop
    print(n)
    n += 1 # soma mais 1



#Exercicio I

numero = int(input('\nDigite o Ultimo numero que será apresentado na tela: '))

n = 0 #inicializando o contador

while n <= numero: #enquanto o numero digitado pelo usuario for menor que N vai ficar no loop
    print(n)
    n += 2 # soma mais 2

 

#Exercicio J

n = int(input('Digite o numero que deseja saber a tabuada: '))
cont = 1 #inicia o contador

print(f'Tabuada do {n}') #fala qual o numero que vai ser multiplicado

while cont <= 10: # enquanto o contator for menor ou igual que 10 ele continua o loop
    resultado = n * cont
    print(f'{n} x {cont} = {resultado}')
    cont += 1 # conta mais 1 no contador

    
    
#exercicio K
        
nt = 0  # Inicializando nt com um valor diferente de -1

while nt != -1:
    nt = int(input('Digite a nota do Aluno(a) (ou digite -1 para sair.): '))

    if nt == -1:
        print('Encerrando programa...')
        break
        
    elif nt < 0 or nt > 100:
        print(f'{nt} é uma nota inválida.')

    else:
        print(f'Nota válida: {nt}')

    """
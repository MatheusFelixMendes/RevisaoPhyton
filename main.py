''' --> Comentario de Bloco
Titulo/ Revisao de Phyton
Autor/ Profe. Berssa
Data/ 2024.07.02
'''
# --> Comentario de linha
# Objetivo/ Revisar os Fundamentos de Programacao em Phyton

print('Hello world!')

# Saida --> print()
print('profe. Berssa Lindu!') # 'string'
print('100 + 100') # 'str'
print(100 + 100) # operacao

# Entrada --> input()
nome = input('Digite seu nome:')
print('Voce disse:', nome)
Valor1 = int(input('Digite um valor: '))
Valor2 = int(input('Digite outro valor:'))
total = Valor1 + Valor2
print('Soma dos valores digitados e:', total)
      
# Variaveis --> espaco de memoria que armazena valores temporariamente
#str --> Armazena textos e caracteres --> %s ou %c
nome = 'Berssa'
print('A variavel nome e do tipo:', type(nome), 'e tem armazenado o valor: %s' %nome)
# int --> Armazena numeros inteiros positivos e negativos --> %d
valorX = -81
print('A variavel valorX e do tipo:', type(valorX), 'e tem armazenado o valor: %d' %valorX)
#float --> Armazena numeros de ponto flutuante  positivos e negativos --> NAO USA , USA . --> %f == %.2f
pi = 3.14159
print('A variavel pi e do tipo', type(pi), 'e tem armazenado o valor: %.2f' %pi)
# bool --> Armazena True ou False
teste = 10 > 50
print('A variavel teste e do tipo:', type(teste), 'e tem armazenado o valor:', teste)

# Operadores
# Aritmeticos --> Calculos +, -, *, /, **, //, %
print(5*5)
print(15/4) # --> resultado float
print(10//3) #--> resultado numero inteiro
print(10%4)
#Atribuicao
A = 10 # --> = (RECEBE)
A += 1 # --> INCREMENTO SOMA 1
A -= 1 # --> DECREMENTO DIMINUI 1
# Relacionais --> Fazem comparacao e retornam True ou False
A == 10 # == e igual == True
A != 10 # diferente == False
# # >; <; >; <=
# # Logicos --> Concatenacao de operadores relacionais
# # and == e; or == ou; not == nao

# # Repeticao
# # laco for --> Quando eu sei quantas vezes vai repetir 
for i in range(11, 102, 2):
  print(i)

palavra = 'Programacao'
for letra in palavra:
  print(letra)

tecla = 1
while tecla != 0: # --> Repete ate a condicao ser False 
  tecla = int(input('Esta no laco While! Digite um numero: '))
  
# Condicao --> if, else, elif
idade = int(input('Informe a idade: '))
if idade >= 18: # Testa e faz se o resultado True
  print('pode ir pro Bailao!')
elif idade >= 16: # Faz se o if == False e o elif == True 
  print('Vai pro Bailao com a Mamae e o Papai!')
else: # Faz se o resultado do if for == a False
  print('Nao vai pro Bailao hoje!')
  
# Funcoes --> def
def soma(x, Y):
  R = X + Y
  return R

 print(soma(10,5))
 print(soma(100, 50))
A = int(input('Digite um valor: '))
B = int(input('Digite um valor; '))
print('Soma de %d e %d e igual a %d' %(A, B, (soma(A, B))))

'''
Problema 1008 (Salário) - Beecrowd
Data: 16/07/2024
Autor: Matheus Felix Mendes
'''
# Objetivo: Calcular o Total a Receber com base na soma do salário a uma comissão das vendas

# Ler o Número de um funcionário 
 NUMBER = input()

# Ler o total de Horas Trabalhadas
Horas = float(input())

# Ler o Valor que recebe por Hora
Valor = float(input())

# Calcular o Salário Total
SALARY = Horas * Valor

# Caucular o Total a Receber == Salario+Comissao
TotalReceber = Salario+Comissao

# Mostrar a mensagem == TOTAL = R$ TotalReceber
print('NUMBER = R$ %.2f' %TotalReceber)
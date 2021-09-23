"""
TUPLAS (tuple)

Tuplas são bem parecidas com listas
Existem basicamente duas diferenças básicas:
1 - As tuplas são representadas por parênteses ()
2 - As tuplas são imutáveis: Isso significa que ao criar uma tupla ela não muda. 
    Toda operação em uma tupla gera uma nova tupla.

"""

#CUIDADO 1: As tuplas são REPRESENTADAS por (), mas veja:
tupla1=(1,2,3,4,5,6) # Cria um tuplas
tupla2=1,2,3,4,5,6   # Também cria uma tupla

#CUIDADO 2: Tuplas com 1 elemento:
tupla3=(4) #Isso não é uma tupla
tupla4=(4,)#Isso É uma tupla

#Podemos gerar uma tupla dinamicamente com o range(início, fim, passo)
tupla = tuple(range(11))
print(tupla)

#Desempacotamento de tupla
tupla-("Geek", "University")
escola, curso = tupla

#Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato
#das tuplas serem imutáveis

#Soma, Máximo, Mínimo e Tamanho, seguem as mesmas regras das listas

#Concatenação de tuplas
tp1=(1,2,3)
print(tp1)

tp2=4,5,6
print(tp2)

print(tp1 + tp2) 

#Devemos utilizar tuplas SEMPRE que não precisamos modificar os dados contidos em uma coleção
#EXEMPLO 
meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')

#Acesso a elementos através de índice é igual às listas

#Por quê utilizar tuplas?

# - Tuplas são mais rápidas do que listas
# - Tuplas deixam seu código mais seguro. Trabalhar com elementos imutáveis traz mais segurança para o código.




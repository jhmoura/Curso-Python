"""
numeros = [5,6,7,8,9]
#Em qual índice está o valor 6?
print(numeros.index(6))
#Em qual índice está o valor 9?
print(numeros.index(9))

#Podemos fazer buscas dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5,1)) #buscando a partir do índice 1
print(numeros.index(5,2)) #buscando a partir do índice 2

"""
#Revisão de slicing
#lista[inicio:fim:passo]
#range(inicio:fim:passo)

#Trabalhando com slice de lista com o parametro início

lista = [1,2,3,4]
print(lista[1:]) #Iniciando no índice 1 e pegando todos os elementos restantes

#Trabalhando com slice de lista com o parametro "fim"
print(lista[:2]) #Começa em 0, pega até o índice 2 -1

#Trabalhando com slice de lista com o parametro "passo"
print(lista[1::2]) # Começa em 1, vai até o fim, de 2 em 2

#Soma, Valor Máximo, Valor Mínimo, Tamanho
#Somente se os valores forem todos inteiros ou reais
lista =[1,2,3,4,5,6]

print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

#Desempacotamento de listas

lista=[1,2,3]
n1, n2, n3 = lista
print(n1)
print(n2) 
print(n3)

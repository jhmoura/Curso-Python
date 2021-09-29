"""
Módulo Collections - Counter

Conhecidos como High-performance Conteiner Datatypes

Recebe um interável como parametro e cria um objeto do tipo Collections COunter
que é parecido com um dicionário, contendo como chave o elemento da lista passada como parametro
e como valor a quantidade de ocorrências desse elemento.


"""

from collections import Counter

lista = [1,1,1,2,2,3,3,3,3,1,1,2,2,4,4,5,5,3,45,1,5,66,66,78,1,65]

res = Counter(lista)
print(res)
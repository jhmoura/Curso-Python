"""
Funções são pequenos trechos de código que realizam tarefas especificas.
Pode ou não receber entrada de dados e retornar uma saída de dados

Já utilizamos várias funções até agora:
print, len, int, min, max, count ...

Em python a forma gerar de definir uma função é:

def nome_da_funcao(parametros-de-entrada):
    bloca da função
# Funções com Retorno

def quadrado_de_7():
    return 7 * 7


#Criamos uma variável para receber o valor do return
ret = quadrado_de_7()

print(f'Retorno {ret}')
"""


# Refatorando a primeira função

def diz_oi():
    return 'Oi!!'


print(diz_oi())

alguem = "Pedro"
print(diz_oi() + alguem)


# Utilizando *args: para declarar usar asterisco, para usar, não coloca asterisco


def soma_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total


print(soma_numeros())
print(soma_numeros(1))
print(soma_numeros(1, 2))
print(soma_numeros(3, 4, 5))
print(soma_numeros(5, 6, 7, 8, 9))


# Refatorado

def soma_numeros(*args):
    return sum(args)


print(soma_numeros())
print(soma_numeros(1))
print(soma_numeros(1, 2))
print(soma_numeros(3, 4, 5))
print(soma_numeros(5, 6, 7, 8, 9))

# Desempacotador

numeros = [1, 2, 3, 4, 5, 6, 7]

# O asterisco irá desempacotar os valores da lista passada como argumento
# Ele informa ao Python que estamos passando uma coleção de dados como argumento
print(soma_numeros(*numeros))

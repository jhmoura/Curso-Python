"""
Dicionários

Em algumas linguagens ded programação, os dicionários python são conhecidos como mapas
Dicionários são coleções do tipo chave/valor

Dicionáriossão representados por {}
OBS.:-Chave e valor são separados por : ;
     -Tanto chave quanto valor pode ser de qualquer tipo de dado;
     -Podemos misturar tipos de dados

"""
paises = {'br':'Brasil', 'eua':'Estados Unidos', 'py':'Python'}

print(paises)

#Acessando elementos
#Acessando via chave
print(paises['br'])
print(paises['py'])

#Acessando via get - RECOMENDADO
#Caso o GET não encontre o objeto com a chave informada, será retornado o valor None
# e não será gerado KeyError
print(paises.get('br'))
print(paises.get('ru'))

#Podmeos definir um valor padrão caso não encontremos o objeto com a chave encontada
pais=paises.get('ru', 'Não encontrado')
print(f'Encontrei o pais {pais}')

#Podemos usar qualquer tipo de dados como chave de dicionários
#Tuplas por exemplo são bem interessantes de serem utilizadas com chaves de dicionário
# pois as mesmas são imutáveis
localidades = {
    (35.6548, 39.1456):'Escritório em Tókio',
    (40.4587, 74.6932):'Escritório em São Paulo',
    (37.1234, 122.44791):'Escritório em Londres',
}

print(localidades)
print(type(localidades))

#Adicionar elementos em um dicionário
receita = {'jan':100, 'fev':120, 'mar':300}
print(receita)
#forma 1 - Mais comum
receita['abr'] = 350
print(receita)

#Forma 2 - 
novo_dado={'mai':500}
receita.update(novo_dado) #receita.update({'mai': 500})
print(receita)

# Em dicionários NÃO PODEMOS ter chaves repetidas, caso a chave já exista, o valor será alterado

#Remover dados de um dicionário
#Forma 1
#receita.pop('mar')
#precisamos informar a chave
# Ao removermos um objeto, o seu valor é sempre retornado

#Forma 2
#del receita['fev'] # Se a chave não existir, será gerado keyerror

 # Métodos de dicionários


d = {'a': 1, 'b': 2, 'c': 3}

#Limpar dicionário
#d.clear()
novo = d.copy()
print(novo)
novo['d'] = 4
print(novo)

#Forma não usual de criação de dicionários
outro = {}.fromkeys('a', 'b')
print(outro)

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
#OBS.: O método .fromkey recebe 2 parâmetros: um interável e um valor.
# Ele vai gerar para cada valor do interável uma chave e irá atribuir a esta chave o valor informado.
# Strings também são interáveis

veja = {}.fromkeys('teste', 'valor')
print(veja)

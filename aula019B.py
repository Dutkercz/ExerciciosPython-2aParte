
pessoas = {'nome':'Cris', 'sexo':'M', 'idade':'32'} #para declarar usamos chaves
print(pessoas['nome'])#para referenciar usamos colcheter (normal)
print(f'O aluno {pessoas["nome"]}, tem {pessoas["idade"]} anos')#tem que usar " (duplas), na formatação
print()
print(pessoas.keys())
print()
print(pessoas.values())
print()
print(pessoas.items())
print()
pessoas['nome'] = 'Cristian' #substituir o valor da variavel, na key = 'nome'
print(pessoas['nome'])
print('==============='*5)
print()
print('DICIONARIO DENTRO DE UMA LISTA')
brasil = []
estado1 = {'nome':'Rio Grande do SUl', 'UF':'RS'}
estado2 = {'nome':'Santa Catarina', 'UF':'SC'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print()
print(brasil[1]['UF'])
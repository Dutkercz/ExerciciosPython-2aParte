dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])
print()
pessoas=list()#declrei uma nova lista
pessoas.append(dados[:]) #posso adicionar uma lista ja feita
#dentro da minha nova lista. utilizando varNOVA.append(ListaCompleta[:])
#o [:] faz uma copia de tudo que há na lista
print(pessoas)
#e posso adicionar mais dados ex:
dados.append('Cristian')
dados.append(32)
pessoas.append(dados[:])#Se eu usar o APPEND. depois de declarar
# a lista DADOS, sera copiado tudo que há na lista dados como 1 espaço só
#em memoria
dados.append('Jenifer')#depois de lançar DADOS na lista PESSOAS
#posso declarar novos dados para a lista DADOS
dados.append(29)
# e esses novos dados irão se transformar e um só dentro da nova lista
#ex
pessoas.append(dados[:])
print(pessoas)
print(pessoas[0][1])#ira mostrar o primeiro item da lista '0', na posição '1'

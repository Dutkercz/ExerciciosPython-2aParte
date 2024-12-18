'''DICIONARIOS USA INDICES LITERAIS'''

'''TUPLAS SÃO IDENTIFICADOS POR {}'''

'''EXEMPLO
dados = dict()
ou
dados = {}  '''
dados = {'nome':'Pedro', 'idade' : '25' }
print(dados['nome'] , dados['idade'])
''' EM DICIONARIOS O VALOR DA VARIAVEL NAO OCUPA UMA POSIÇÃO NUMERICA, MAS SIM UM POSIÇÃO LITERAL'''
'''NO EXEMPLO ACIMA, CHAMAMOS A VARIAVEL E EM SEGUIDA A SUA PALAVRA ATRIBUIDA, 
AO INVES DE #PRINT(DADOS[0])'''

'''PARA ADICIONAR ITENS A VARIAVEL (dados), SIMPLESMENTE USAMOS O COMANDO'''
dados['sexo'] = 'M'#ira criar um espaço na mem. da variavel com a informação atribuida
print(dados['sexo'])

'''PARA APAGAR DADOS USAMOS O COMANDO: '''
del dados['sexo']# deleta seu valor, e seu espaço na variavel (OBS: usar espaço entre DEL nome da variavel)
print(dados)
print()
print()
'''POSSO ABRIR '{' E FECHALO EM OUTRA LINHA'''
'''TEMOS 3 OPÇOES PARA A NOSSA VARIAVEL'''
#USANDO O EXMPLO ABAIXO

'''.values() ira chamar todos o valores, no causo abaixo, 'star wars', '1977', 'jorge lucas' '''
'''.keys() que ira chamar os valores 'titulo', 'ano', 'diretor', '''
'''.items() que ira chamar os dois valores, VALUES E KEYS'''
filmes = {'titulo':'star wars',
          'ano':'1977',
          'diretor':'jorge lucas'
}
print(filmes.values())
print(filmes.keys())
print(filmes.items())
print()
''' USANDO O FOR'''
for k, v in filmes.items(): #temos que usar o .items() para ele por no laço tudo que pertence ao dic.
    print(f'O {k} é {v}')#para cada K = keys, no dic. filmes, eu uso o seu V(valor da key)
#ira mostar a informções do dicionario em ordem
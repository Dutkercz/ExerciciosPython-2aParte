#LISTAS
'''LISTAS
VARIAVEIS COMPOSTAS!'''

'''LISTAS USAM [] e PODEM SER ALTERADAS!!!'''

lanche = ['banana', 'cafe', 'açucar' ,'leite']
print(lanche)
lanche[0]='laranja'# em listas eu posso mudar o valor
print(lanche)#utilizando a posição em que se encontra na variavel
print()
lanche.append('bolacha')#posso tambem adicionar
print(lanche)#O comando .append() adiciona item no final da lista, e empurra os demais pro inicio
print()
lanche.insert(0,'salgado')
print(lanche)# o comando .insert() adiciona um item na posição especificada
print()
del lanche[1]#comando para apagar um item
'''pode usar os comando LANCHE.POP(1) / LANCHE.REMOVE('LARANJA')
NO COMANDO .REMOVE('') TEM QUE ESCREVER O NOME DO VALOR'''
print(lanche)
lanche.pop()#remove o ultimo item
if 'pizza' in lanche: #só ira remover pizza se ela estiver na lista
    lanche.remove('pizza')
'''Podemos criar lista com o laço RANGE:'''
valores = list(range(4,11))#vai criar um lista com esses numeros 4 ao 10
print(valores)
print()

valores2 = [8,2,5,5,9,3,0]
valores2.sort()#coloca os valores em ordem, cres. ou alfa
valores2.pop(4)#retira o item na posição 4
valores2.remove(5)#retira um dos numeros 5, o primeiro
print(valores2)
valores2.sort(reverse=True)#cria em ordem contraria\DESCRESCENTE
print(valores2)
print(len(valores2))
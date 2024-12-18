'''INTERACTIVE HELP'''
#tem por objetivo ajudar usuarios que usam as bibliotecas importadas

#help(print()) < mostra a docstring do print
#print(input.__doc__)


def contador (i, f, p):#para isensir uma docstring na minha função, inicio com aspas 3x e quebro e linhq
    '''
    faz uma contagem de i até f, com passo 'p', e mostra na tela
    :param i: inicio da contagem.
    :param f: final da contagem.
    :param p: passo, ou pulo da contagem.
    :return: sem retorno
    '''
    while i < f:
        print(i)
        i+=p
    print('fim')



contador(1, 10, 2) #parametros formais
help(contador)


'''PARAMETROS OPCIONAIS'''

def somar(a, b , c=0):# portanto o C se torna opcional, e a função vai funcionar normalmente
    s = a + b + c     #podemos aplicar a todos os 3 elementos a, b, c
    print(s)

somar(1,3,4) #porem nao pode receber mais que 3


'''ESCOPO DE VARIAVEIS'''
''' BASICAMENTE: VARIAVEIS DENTRO DE FUNÇÕES, SÓ VALEM DENTRO DAS FUNÇÕES, AO CONTRARIO DE VARIAVEIS NO PROGRAMA 
PRINCIPAL, ELAS ABRANGEM O PROGRAMA INTEIRO, E SEU VALOR PODE SER USADO DENTRO DAS FUNÇÕES'''
def teste():
    print(f'Na função teste N vale {n}')#VARIAVEIS ESCOPO LOCAL

#Programa principal < VARIAVEIS COM ESCOPO GLOBAL
n = 2
print(n)
teste()
print()
print()
'''RETURN'''
def somar (a=0, b=0, c=0):
    s = a + b + c # para apresentar o result. na tela, teria que ter um print logo abaixo, porem seria 1 por linha
    return s # print(s)  ao invez disso eu uso o resturn,

r1 = somar(1,3)   #associo o meu 'return s' a uma variavel.
r2 = somar(3, 4 , 5)
r3 = somar(1)
print(f'Meus calculos foram {r1}, {r2} e {r3}')
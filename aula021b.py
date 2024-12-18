def somar (b):
    a = 8 #posso criar uma variavel igual dentro da minha função com valor diferente
    c = 2
    b += 4 #somou com o 'a' fora da def, pois chamei a função no prog. princ. passando o 'a' de fora como parametro
    print(f' a dentro vale {a}')
    print(f' b dentro vale `{b}')
    print(f' c dentro vale {c}')

a=3
somar(a)
print(f' a fora vale {a}')

print('=====================')
def somar (b):
    global a # faz a var. 'a' ter o valor que esta declaro na função, mesmo fora no escopo da def
    a = 8 #posso criar uma variavel igual dentro da minha função com valor diferente
    c = 2
    b += 4 #agora ira somar com o 'a' que esta declaro na função
    print(f' a dentro vale {a}')
    print(f' b dentro vale `{b}')
    print(f' c dentro vale {c}')

a=3 #perde seu valor apos declarar na função que 'global a'  a = 8
somar(a)
print(f' a fora vale {a}')
print('=======')
somar(a)
print(f' a fora vale {a}')
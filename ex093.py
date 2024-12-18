
golpp =[]
jogador = {}
total=0

jogador['Nome'] = str(input('Nome do Jogador: ')).strip().title()#1 - colocando a o nome do jogador no dicionario posição 'Nome'.
np = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))#2 - captando o numero de partidas.

for c in range (0,np):#in range com o 'np' numero de partidas para saber a quant. de gols em cada jogo.
    golpp.append(int(input(f'    Gols marcados na partida {c+1}: ')))#utiliza um lista para guardar os 'gols'
    jogador['gols']=golpp#depois da lista pronta, atribui a uma posição no dicionario.

print('*=*'*20)
for c in range (0, len(golpp)):#in range com o tamanho da lista, para somar os gols
    total+=golpp[c]
    
# ou usar a função sum >> jogador['total de gols'] = sum(golpp), dai nao precisa a parte de baixo \/

jogador['total de gols']=total#atribui esse total de gols a uma posição no dicionario 'total de gols'

print(jogador)
print('*=*'*20)

for k, valk in jogador.items():#para cada k(key) o valk(valor da key).
    print(f'{k} : {valk}')
print('*=*'*20)

for i, v in enumerate (golpp):#para apresentar os valores de cada posição na lista dos gols (golpp)
    print(f'=> Na partida {i+1}, {jogador["Nome"]} fez {v} gols.')
print(f'Um total de {jogador["total de gols"]} gols')
print('*=*'*20)

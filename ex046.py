from time import sleep
print('Contagem REGRESSIVA PARA O FIM DO ANO')
for c in range (10, -1, -1):
    print('\033[34m',c,'\033[m')
    sleep(1)
print('\033[32m FELIZ ANO NOVO!! \033[m')
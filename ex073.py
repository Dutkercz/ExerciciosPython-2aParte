from operator import index

times = ('Botafogo','Palmeiras','Fortaleza','Internacional','Flamengo','São Paulo','Cruzeiro','Bahia','Vasco','Corinthians','Atlético-MG','Grêmio','Vitória','Fluminense','Criciúma','Juventude','Bragantino','Athletico-PR','Cuiabá','Atlético-GO')
print(f'Lista de times do Brasileirão em ordem de colocação{times}')
print(f'Os 5 primeiros são{times[0:6]} ')
print(f'Os 4 na Zona do REBAIXAMENTO são {times[-4:]}')
#gremio = times.index('Grêmio')
print(f'O Grémio está em {times.index('Grêmio')+1}°')
print(f'Os time por ordem Alfabetica são: {sorted(times)}')
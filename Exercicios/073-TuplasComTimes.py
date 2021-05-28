times = ('Flamengo','Internacional','Atlético-MG','São Paulo','Fluminense','Grêmio',
         'Palmeiras','Santos','Athletico-PR','Bragantino,Ceará','Corinthians','Atlético-GO',
         'Bahia','Sport','Fortaleza','Vasco','Goiás','Coritiba','Botafogo')
print('-=-'*50)
print(f'Listas de Times do Brasileirão: {times}')
print('-=-'*50)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=-'*50)
print((f'Os 4 Ultimos são: {times[-4: ]} '))
print('-=-'*50)
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O Chapecoense está na {times.index("Coritiba")+1} ª posição')
print('-=-'*50)

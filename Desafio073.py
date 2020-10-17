times = ('Atlético-MG','Internacional', 'Flamengo','São Paulo','Fluminense','Santos',
         'Palmeiras','Fortaleza','Atlético-GO','Sport','Grêmio','Vasco','Ceará','Corinthians',
         'Botafogo','Bahia','Coritiba','Athletico-PR','Bragantino','Goiás')
print('='*30)
print(f'O 5 primeiros colocados são {times[0:5]}')
print('='*30)
print(f'Os últimos 4 colocados {times[-4:]}')
print('='*30)
print('Os times em ordem alfabética são:', sorted(times))
print('='*30)
print(f'O time Fluminense está na {times.index("Fluminense")+1}° colocação')
print('='*30)
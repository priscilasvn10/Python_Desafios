esta = {}
partida = []
esta['nome'] = str(input('Nome do Jogador: '))
nun = int(input(f'Quantas partidas {esta["nome"]} jogou? '))
for c in range(0, nun):
    partida.append(int(input(f'Quantos gols na partida {c}? ')))
esta['gols'] = partida[:]
esta['total'] = sum(partida)
print('-='*30)
print(esta)
print('-='*30)
for k, v in esta.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {esta["nome"]} jogou {len(esta["gols"])} partidas.')
for i,c in enumerate(esta['gols']):
    print(f' => Na partida {i}, fez {c} gols.')
print(f'Foi um total de {esta["total"]} gols.')

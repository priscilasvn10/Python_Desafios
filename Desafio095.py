jogador = {}
partida = []
dados = []
while True:
    print('-' * 30)
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    nun = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partida.clear()
    for c in range(0, nun):
        partida.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    dados.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro. Digite somente S ou N.')
    if resp == 'N':
        break
print('-='*40)
print('Cod    ',end='')
for i in jogador.keys():
    print(f'{i:<13}', end='')
print()
print('-'*40)
for i,v in enumerate(dados):
    print(f'{i:<7}',end='')
    for d in v.values():
        print(f'{str(d):<14}', end='')
    print()
while True:
    print('-' * 40)
    n = int(input('Mostrar dados de qual jogador? (999 sai)'))
    if n == 999:
        break
    if n >= len(dados):
        print(f'ERRO! Não existe jogador com código {n}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {dados[n]["nome"]:}')
        for i, g in enumerate(dados[n]["gols"]):
            print(f' => No jogo {i+1} fez {g} gols.')
print('------- FIM -------')

def ficha(nome='<desconhecido>', gol=0):
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0
    if nome.strip() == '':
        nome = '<desconhecido>'
    return f'O jogador {nome} fez {gol} gol(s) no campeonato.'


print('-'*30)
n = str(input('Nome do Jogador: '))
g = str(input('Números de Gols: '))
print(ficha(n, g))
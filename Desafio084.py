dados = []
total = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(total) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    total.append(dados[:])
    dados.clear()
    res = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if res in 'N':
        break
print('='*40)
print(f'Foram cadastradas {len(total)} pessoas')
print(f'O maior peso é {maior} Kg. De ', end='')
for p in total:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso é {menor} Kg. De ', end='')
for p in total:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')

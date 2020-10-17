tot = cont = c =0
print('='*30)
print('Loja Aqui você encontra!')
print('='*30)
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço: R$ '))
    tot += preco
    c += 1
    if preco > 1000:
        cont += 1
    if c == 1 or preco < barato:
        barato = preco
        no = nome
    res = ' '
    while res not in 'SN':
        res = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if res == 'N':
        break
    print('='*30)
print('*'*30)
print(f'O total gasto foi R$ {tot:.2f}')
print(f'Foram {cont} produtos mais de R$ 1000,00 ')
print(f'O produto mais barato foi {no} por R$ {barato:.2f}.')
print('*'*5, 'Agradecemos a preferência. Volte sempre!','*'*5)
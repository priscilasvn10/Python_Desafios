matriz=[[0,0,0],[0,0,0],[0,0,0]]
par = ter = ma = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor [{l}][{c}]: '))
        if matriz[l][c] % 2 == 0 :
            par += matriz[l][c]
        if c == 2:
            ter += matriz[l][c]
        if l == 1:
            if ma < matriz[l][c]:
                ma = matriz[l][c]
print('=-'*30)
for l in range (0,3):
    print()
    for c in range(0,3):
        print(f'[ {matriz[l][c]} ] ',end='')
print()
print('=-' * 30)
print(f'A soma de todos os valores pares é {par}')
print(f'A soma da terceira coluna é {ter}')
print(f'O maior valor da segunda linha é {ma}')

n1 = []
n2 = []
n3 = []
while True:
    n1.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if r in 'N':
        break
print('='*40)
print(f'A lista digitada é: {n1}')
for i, val in enumerate(n1):
    if val % 2 == 0:
        n2.append(val)
    elif val % 2 == 1:
        n3.append(val)
print(f'A lista de pares é: {n2}')
print(f'A lista de impares é: {n3}')
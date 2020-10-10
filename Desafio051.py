print('='*20)
print('10 termos de uma PA')
print('='*20)

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
de = p + (10-1) * r
for c in range (p, de + r, r):
    print('{}'.format(c), end=' - ')
print('Acabou!')
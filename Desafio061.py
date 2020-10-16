print('='*20)
print('10 termos de uma PA')
print('='*20)

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1
termo = p
while cont <= 10:
   print('{}'.format(termo), end=' → ')
   cont += 1
   termo += r
print('Acabou!')


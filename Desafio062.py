print('='*20)
print('10 termos de uma PA')
print('='*20)

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1
termo = p
n = 10
total = 0
while n != 0:
    total += n
    while cont <= total:
       print('{}'.format(termo), end=' → ')
       cont += 1
       termo += r

    print('Pausa!')
    n = int(input('Quantos termos você quer mostar mais? '))
print('Pregressão finalizada com {} termos mostrados!'.format(total))
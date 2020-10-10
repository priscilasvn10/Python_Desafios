n = int(input('Digite um número: '))
s=0
for c in range (1, n +1):
    if n % c == 0:
        print('\033[33m', end='')
        s +=1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[0mO número {} foi divisível {} vezes'.format(n,s))
if s == 2:
    print('É PRIMO!')
else:
    print('NÃO é primo!')

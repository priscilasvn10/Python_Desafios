from random import randint
from time import sleep
print('='*12,'VAMOS JOGAR JOKEMPÔ','='*12)
lista = ('Pedra','Papel','Tesoura')
computador = randint(0, 2)

print(' [ 0 ] Pedra\n [ 1 ] Papel\n [ 2 ] Tesoura')
n = int(input('Escolha uma opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-='*11)
print('Computador jogou {}'.format(lista[computador]))
print('Você jogou {}'.format(lista[n]))
print('-='*11)
print()
if computador == 0:
    if n == 0:
        print('EMPATE!')
    elif n == 1:
        print('Você VENCEU!')
    elif n == 2:
        print('Você PERDEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if n == 0:
        print('Você PERDEU!')
    elif n == 1:
        print('EMPATE!')
    elif n == 2:
        print('Você VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if n == 0:
        print('Você VENCEU!')
    elif n == 1:
        print('Você PERDEU!')
    elif n == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')

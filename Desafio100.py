from random import randint
from time import sleep
lista = []
def sorteio():
    print(f'Sorteando 5 valores da lista: ', end='')
    for n in range(1,6):
        sleep(0.3)
        x = randint(1,10)
        print(f'{x} ',end='')
        lista.append(x)
    print('Pronto!')


def somaPar():
    soma = 0
    for i in lista:
        if i % 2 == 0:
           soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteio()
somaPar()

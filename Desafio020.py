import random
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarta nome: ')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
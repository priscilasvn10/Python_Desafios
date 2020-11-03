import random
lista = [0,1,2,3,4,5]
escolhido = random.choice(lista)
n = int(input('Tente acertar o número entre 0 e 5: '))
if n==escolhido:
    print('Parabéns você VENCEU!')
else:
    print('Que pena você PERDEU!')
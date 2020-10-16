from random import randint

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
computador = randint(0,10)
acertou = False
cont = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    cont +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas'.format(cont))
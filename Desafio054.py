from datetime import date
atual = date.today().year
s = 0
for c in range (1,8):
    ano = int(input('Digite o {}º ano de nascimento: '.format(c)))
    if atual - ano < 21:
        s +=1
print('{} pessoas não são maiores de idade!'.format(s))
print('{} pessoas já são maiores de idade!'.format(7-s))
f = str(input('Digite uma frase: ')).strip().upper()
separa = f.split()
junto = ''.join(separa)
inverte = ''
'''inverte = junto[::-1] feito sem for'''
for letra in range(len(junto)-1,-1,-1):
    inverte += junto[letra]
print('O inverso de {} é {}'.format(junto, inverte))
if inverte == junto:
    print('É um PALÍNDROMO!')
else:
     print('NÃO é um PALÍNDROMO!')


import math
o = float(input('Comprimento do cateto oposto: '))
a = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(o,a)
#hi = (o** 2 + a**2)**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
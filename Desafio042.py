
p = float(input('Primeiro segmento: '))
s = float(input('Segundo segmento: '))
t = float(input('Terceiro segmento: '))

if p < s + t and s < p + t and t < p + s:
    print('Os segmentos PODEM FORMAR triângulo')
    if p == t == s:
        print('Triângulo EQUILÁTERO!')
    elif p == s or p == t or s == t:
        print('Triângulo ISÓSCELES!')
    elif p != s and p != t and s != t:
        print('Triângulo ESCALENO!')
else:
    print('Os segmentos NÃO PODEM FORMAR TRIÂNGULO')
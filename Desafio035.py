print('-='*20)
p = float(input('Primeiro segmento: '))
s = float(input('Segundo segmento: '))
t = float(input('Terceiro segmento: '))
print('-='*20)

if p < s + t and s < p + t and t < p + s:
    print('Os segmentos PODEM FORMAR triângulo')
else:
    print('Os segmentos NÃO PODEM FORMAR TRIÂNGULO')
def área(l, c):
    area = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {area}m².')


print('  Controle de Terrenos')
print('-'*30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l,c)

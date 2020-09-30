la = float(input('Largura da parede: '))
al = float(input('Altura da parede: '))
area = la*al
ti = area/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(la,al,area))
print('Para pintar essa parede você precisará de {}L de tinta'.format(ti))
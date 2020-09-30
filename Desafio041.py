ano = int(input('Digite o ano de nascimento do atleta: '))

idade = 2020 - ano

if idade < 9:
    print('Categoria MIRIM!')
elif idade<=14:
    print('Categoria INFANTIL!')
elif idade <=19:
    print('Categoria JUNIOR!')
elif idade <=20:
    print('Categoria SÊNIO!')
else:
    print('Categoria MASTER!')




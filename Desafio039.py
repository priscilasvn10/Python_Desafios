ano = int(input('Digite o seu ano de nascimento: '))
m = 2020 - ano
if m < 18:
    a = 18 - m
    print ('Você ainda vai se alistar ao Serviço Militar daqui a {} anos'.format(a))
elif m == 18:
    print('É a hora de se alistar para o Serviço Militar!')
else:
    b = m - 18
    print('Já passou o tempo {} anos para o Alistamento Militar'.format(b))
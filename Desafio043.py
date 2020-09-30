peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = (peso/ (altura*altura))

if imc <18.5:
    print('Você está com {:.2f}, está abaixo do peso!'.format(imc))
elif imc>= 18.5 and imc <25:
    print('Você está com {:.2f}, está no peso ideal!'.format(imc))
elif imc >=25 and imc <30:
    print('Você está com {:.2f}, está com Sobrepeso!'.format(imc))
elif imc >=30 and imc<40:
    print('Você está com {:.2f}, está com O besidade!'.format(imc))
else:
    print('Você está com {:.2f}, está com Obesidade Mórbida!'.format(imc))


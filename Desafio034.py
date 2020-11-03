salario = float(input('Digite o salário: R$  '))
if salario>1250:
    calc = salario + salario * 0.10
    print('O novo salário é de R$ {:.2f}'.format(calc))
else:
    calc = salario + salario * 0.15
    print('O novo salário é de R$ {:.2f}'.format(calc))
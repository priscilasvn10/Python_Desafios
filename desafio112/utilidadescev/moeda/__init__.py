def aumentar(valor=0, aumento=0, formato = False):
    '''
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param valor: o preço que se quer reajustar
    :param aumento: qual é a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    '''
    res =valor + (valor * aumento/100)
    return res if formato == False else moeda(res)


def diminuir(valor=0, dimi=0,  formato = False):
    res = valor - (valor * dimi/100)
    return res if formato == False else moeda(res)


def dobro(valor=0,  formato = False):
    res = valor *2
    return res if formato == False else moeda(res)


def metade(valor=0,  formato = False):
    res = valor/2
    return res if formato == False else moeda(res)


def moeda(valor=0, moeda = 'R$'):
    return f'{moeda}{valor:>7.2f}'.replace('.',',')


def resumo(valor=0, aum=10, dimi=5):
    print('-'*30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor,True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aum}% de aumento: \t{aumentar(valor,aum,True)}')
    print(f'{dimi}% de redução: \t{diminuir(valor, dimi,True)}')
    print('-' * 30)
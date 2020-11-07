def aumentar(valor=0, aumento=0):
    res =valor + (valor * aumento/100)
    return res


def diminuir(valor=0, dimi=0):
    res = valor - (valor * dimi/100)
    return res


def dobro(valor=0):
    res = valor *2
    return res


def metade(valor=0):
    res = valor/2
    return res


def moeda(valor=0, moeda = 'R$'):
    return f'{moeda}{valor:>8.2f}'.replace('.',',')
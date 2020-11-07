def aumentar(valor=0, aumento=0, formato = False):
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
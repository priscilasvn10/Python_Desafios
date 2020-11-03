def notas(*nota,sit=False):
    """-> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma."""
    dic = {}
    dic['total'] = len(nota)
    dic['maior'] = max(nota)
    dic['menor'] = min(nota)
    dic['soma'] = sum(nota) / len(nota)
    if sit == True:
        if dic["soma"] >= 7:
            dic['situação'] = 'BOA'
        elif dic["soma"] >= 5:
            dic['situação'] = 'RAZOÁVEL'
        else:
            dic['situação'] = 'RUIM'
    return dic


resp = notas(3.5, 10, 0.5, 9.5, sit=True)
print(resp)
help(notas)

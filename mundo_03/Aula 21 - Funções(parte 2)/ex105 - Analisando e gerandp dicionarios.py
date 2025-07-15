def notas(*n,sit=False):
    '''
    -> notas = função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve o não adicionar a situação
    :return: dicionário com várias iinformações sobre a situação da turma.
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação']='BOA'
        elif r['média'] >= 5:
            r['situação']='Razoavel'
        else:
            r['situação']='Ruim'
    return r


#ProgramaPrincipal
resp = notas(5.5,2.5,9,8.5, sit=True)
print(resp)
help(notas)
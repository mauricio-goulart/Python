def notas(*num, sit = False):
    """
    :param num: numeros das notas
    :param sit: mostrar ou nao a situacao
    :return: retorna a lista
    """
    alunos = dict()
    alunos['total'] = len(num)
    alunos['maior'] = max(num)
    alunos['menor'] = min(num)
    alunos['media'] = sum(num) / len(num)
    if sit:
        if alunos['media'] >= 6.5:
            alunos['situacao'] = 'Aprovado'
        else:
            alunos['situacao'] = 'Reprovado'



    return alunos




print('-' * 30)
n = notas(8, 9, sit= True)
print(n)
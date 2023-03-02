alunos = dict()
print('-=' * 20)
alunos['Nome'] = str(input('Nome: '))
alunos['Media'] = float(input(f'Media de {alunos["Nome"]}: '))
if alunos['Media'] >= 7.0:
    alunos['Situação'] = 'Aprovado'
elif 5 <= alunos['Media'] < 7:
    alunos['Situação'] = 'Recuperação'
else:
    alunos['Situação'] = 'Reprovado'
print('-=' * 20)
for k,v in alunos.items():
    print(f'{k} = {v}')
print('-=' * 20)

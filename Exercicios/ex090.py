alunos = dict()
talunos = list()
print('-=' * 5, 'Media','=-' * 5)
alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input(f'Media de {alunos["nome"]}: '))
print('-=' * 14)
for k,v in alunos.items():
    print(f'{k} = {v}')
if alunos['media'] > 6.5:
    print('[Aprovado]')
else:
    print('[Reprovado]')
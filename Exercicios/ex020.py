import random

a1 = str(input('Nome do Aluno: '))
a2 = str(input('Nome do Aluno: '))
a3 = str(input('Nome do Aluno: '))
a4 = str(input('Nome do Aluno: '))

print(f'{"ORDEM DE APRESENTAÇÃO":=^40}')

list = [a1, a2, a3, a4]
esc = random.shuffle(list)

print(list)
print('=' * 40)
import random

a1 = input('Nome do Aluno: ')
a2 = input('Nome do Aluno: ')
a3 = input('Nome do Aluno: ')
a4 = input('Nome do Aluno: ')

list = 'a1 a2 a3 a4'.split()
esc = random.shuffle(list)

print(list)
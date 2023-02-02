nome = str(input('Digite seu nome: '))

if nome == 'Mauricio' or nome in 'Maria':
    print('Que nome lindo')
elif nome == 'Carlos' or nome == 'Petry':
    print('Nome bem normal')
else:
    print('Nome bem normal')

print(f'Bom dia {nome}')

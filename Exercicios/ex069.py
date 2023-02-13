c = 1
cond = ''
sexo = ''
while True:
    print(f'---- {c}ºPessoa ----')
    c = c + 1
    nome = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] '))
    while sexo not in 'MmFf':
        print('SEXO INVALIDO')
        sexo = str(input('Sexo: [M/F] '))

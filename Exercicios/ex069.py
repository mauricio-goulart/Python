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
    cond = str(input('Quer continuar?: [S/N] '))
    while cond not in 'SsnN':
        print('DIGITE CERTO')
        cond = str(input('Quer continuar?: [S/N] ')).strip().lower()
    if cond == 'n':
        break

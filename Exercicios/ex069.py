c = 1
cond = ''
sexo = ''
midade = 0
toth = 0
while True:
    print(f'---- {c}ºPessoa ----')
    c = c + 1
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().lower()
    while sexo not in 'MmFf':
        print('SEXO INVALIDO')
        sexo = str(input('Sexo: [M/F] '))
    cond = str(input('Quer continuar?: [S/N] '))
    while cond not in 'SsnN':
        print('DIGITE CERTO')
        cond = str(input('Quer continuar?: [S/N] ')).strip().lower()
    if idade > 18:
        midade = midade + 1
    if sexo == 'm'
    if cond == 'n':
        break


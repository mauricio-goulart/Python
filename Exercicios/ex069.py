c = 1
cond = ''
sexo = ''
midade = 0
toth = 0
fidade = 0
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
    if sexo == 'm':
        toth = toth + 1
    if sexo == 'f' and idade < 20:
        fidade = fidade + 1
    if cond == 'n':
        break
print('-' * 20)
print(f'Maiores de idade: [{midade}]')
print(f'Total Homens: [{toth}]')
print(f'Mulheres menor de 20: [{fidade}]')
print('-' * 20)

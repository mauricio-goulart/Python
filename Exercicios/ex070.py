print('\tLOJA SUPER BARATO\n')
c = 1
totp = 0
maiorp = 0
nomemenor = ' '
menorp = 0
cond = ''
while True:
    print(f'----- {c}ºPRODUTO -----')
    c = c + 1
    nomep = str(input('Nome: '))
    precop = int(input('Preço: '))
    if precop > 1000:
        maiorp = maiorp + 1
    if c == 2 :
        nomemenor = nomep
        menorp = precop
    else:
        if menorp > precop:
            nomemenor = nomep
            menorp = precop

    cond = str(input('Quer continuar? [S/N] ')).strip().lower()
    totp = totp + precop
    if cond == 'n':
        break

print('-' * 20)
print(f'Total:[{totp}]')
print(f'Produto mais barato:[{nomemenor}]')
print(f'Quantos produtos maiores que R$1000:[{maiorp}]')



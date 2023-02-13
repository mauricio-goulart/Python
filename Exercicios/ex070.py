print('\tLOJA SUPER BARATO\n')
c = 1
totp = 0
maiorp = 0
nomemenor = ''
menorp = 0
cond = ''
while True:
    print(f'----- {c}ºPRODUTO -----')
    c = c + 1
    nomep = str(input('Nome: '))
    precop = int(input('Preço: '))
    if precop > 1000:
        maiorp = maiorp + 1
    if menorp > precop:
        nomemenor = nomep
    cond = str(input('Quer continuar? [S/N] ')).strip().lower()
    if cond == 'n':
        break


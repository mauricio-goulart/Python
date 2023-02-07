r = 's'
c = 0
while r == 's':
    c = c + 1
    print(f'---- {c}ºPESSOA ----')
    sexo = str(input('Sexo:[M/F]')).upper()
    if sexo != 'M' and sexo != 'F':
        print('DIGITE UM SEXO VÁLIDO:')


    r = str(input('Continuar: [s/n]'))
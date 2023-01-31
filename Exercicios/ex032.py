ano = int(input('Digite um ano: '))
print(f'{"Bissexto":=^20}')
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'[BISSEXTO]')
else:
    print('[NÃO É BISSEXTO]')
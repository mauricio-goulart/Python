n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('-=' * 15)
if (n1+n2) / 2 < 5:
    print(f'Media:[{(n1+n2) / 2 }]')
    print('[REPROVADO]')
elif (n1+n2) / 2 >= 7:
    print(f'Media:[{(n1+n2) / 2}]')
    print('[APROVADO]')
elif (n1+n2) / 2 > 5 and (n1+n2) / 2 < 6.9:
    print(f'{(n1+n2) / 2}')
    print('[RECUPERACAO]')
print('-=' * 15)
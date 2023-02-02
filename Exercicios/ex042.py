r1 = float(input('Tamanho da reta: '))
r2 = float(input('Tamanho da reta: '))
r3 = float(input('Tamanho da reta: '))
print(f'{"Analisando":=^20}')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Formam um [Triangulo]', end='')
    if r1 == r2 == r3 :
        print('[EQUILÁTERO]')
    elif r1 != r2 != r3 != r1 :
        print('[ESCALENO]')
    elif r1 != r2 != r3:
        print('[ISÓSCELES]')


else:
    print('Não forma')
print('=' * 20)
n = 0
cont = 0

n = int(input('Quer ver a tabuada de qual valor? '))
print('-=' * 15)
while True:
    for cont in range(0,11):
        print(f'\t{n} x {cont} = {n * cont}')
    print('-=' * 15)
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
print('-=' * 15)
print('PROGRAMA DE TABUADA ENCERRADA')
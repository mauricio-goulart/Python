n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1

print(f'Calculando [{n}]!:')
while c > 0 :
    print(f'{c}')
    if c > 1:
        print(' x ')
    else:
        print(' = ')

    f = f * c
    c = c - 1
print(f'{f}')


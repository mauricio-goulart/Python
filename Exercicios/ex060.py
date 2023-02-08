n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1

print(f'Calculando [{n}]!:', end=' ')
while c > 0 :
    print(f'{c}', end=' ')
    if c > 1:
        print(' x ', end=' ')
    else:
        print(' = ', end=' ')

    f = f * c
    c = c - 1
print(f'{f}', end=' ')


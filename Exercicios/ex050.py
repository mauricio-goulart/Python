s = int(0)
c = int(0)
pares = int(0)

print('-=' * 15)
print('Contador números pares')
print('-=' * 15)

for contador in  range(0,6):
    c = c + 1
    n1 = int(input(f'Número [{c}]:'))
    if n1 % 2 == 0:
        pares = pares + 1
        s = s + n1

print('-=' * 15)
print(f'Soma:[{s}]')
print(f'Números Pares:[{pares}]')
print('-=' * 15)


n = 0
s = 0
cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break

    cont = cont + 1
    s = n +s

print(f'Soma:[{s}]')
print(f'Quantidade de números:[{cont}]')
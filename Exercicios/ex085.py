num = [[], []]
totp = 0
toti = 0
valor = 0

print(f'{"IMPAR OU PAR":=^20}')

for c in range (1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)


print(f'Valores pares: {num[0]}')
print(f'Valores Impares: {num[1]}')

n = int(input('Digite um número: '))

print(f'{"Analisando":=^20}')

print(f'Unidade:[{n // 1 % 10}]')
print(f'Dezena:[{n // 10 % 10}]')
print(f'Centena:[{n // 100 % 10}]')
print(f'Milhar:[{n // 1000 % 10}]')
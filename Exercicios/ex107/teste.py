import moeda

print('-=' * 15)
m = float(input('Digite o preço: '))
print('-=' * 15)
print(f'A metade de [{m}]: {moeda.metade(m):.2f}')
print(f'O dobro de [{m}]: {moeda.dobro(m)}')
print(f'O triplo de [{m}]: {moeda.triplo(m)}')
print(f'Aumentando 10% de [{m}]: {moeda.aumenta(m, 10)}')
print(f'Retirando 13% de [{m}]: {moeda.retira(m,13)}')
print('-=' * 15)

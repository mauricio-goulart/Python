import moeda

print('-=' * 15)
m = float(input('Digite o preço: '))
print('-=' * 15)
print(f'A metade de [{moeda.moeda(m)}]: {moeda.moeda(moeda.metade(m))}')
print(f'O dobro de [{moeda.moeda(m)}]: {moeda.moeda(moeda.dobro(m))}')
print(f'O triplo de [{moeda.moeda(m)}]: {moeda.moeda(moeda.triplo(m))}')
print(f'Aumentando 10% de [{moeda.moeda(m)}]: {moeda.moeda(moeda.aumenta(m, 10))}')
print(f'Retirando 13% de [{moeda.moeda(m)}]: {moeda.retira(m,13)}')
print('-=' * 15)

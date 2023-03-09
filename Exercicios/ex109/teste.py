import moeda

print('-=' * 15)
m = float(input('Digite o preço: '))
print('-=' * 15)
print(f'A metade de [{moeda.moeda(m)}]: {moeda.metade(m,True)}')
print(f'O dobro de [{moeda.moeda(m)}]: {moeda.dobro(m,True)}')
print(f'O triplo de [{moeda.moeda(m)}]: {moeda.triplo(m,True)}')
print(f'Aumentando 10% de [{moeda.moeda(m)}]: {moeda.aumenta(m, 10 , True)}')
print(f'Retirando 13% de [{moeda.moeda(m)}]: {moeda.retira(m,13, True)}')
print('-=' * 15)

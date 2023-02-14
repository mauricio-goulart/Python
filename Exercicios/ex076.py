listagem = ('RTX 2060',1500,
            'RTX 3070 TI',2900,
            'RTX 4080 TI',6000,
            'RYZEN 7 2700',1000,
            'INTEL I7 7700',1500,
            'HOGWARTS LEGACY PC',250,
            'HOGWARTS LEGACY DELUXE PC',300)
print('-' * 40)
print(f'{"LOJA DO MAURICIO":^40}')
print('-' * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)

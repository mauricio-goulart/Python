lanche = 'Hamburguer', 'Pizza', 'Suco', 'Pudim'

for cont in range(0,len(lanche)):
    print(f'{lanche[cont]} na pos {cont}')

for pos, comida in enumerate(lanche):
   print(f'{comida} na pos {pos}')
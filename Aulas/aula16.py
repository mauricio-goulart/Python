lanche = 'Hamburguer', 'Pizza', 'Suco', 'Pudim'

for cont in range(0,len(lanche)):
    print(f'{lanche[cont]} na pos {cont}')

for pos, comida in enumerate(lanche):
   print(f'{comida} na pos {pos}')


a = [1,2,3,4]
b = [5,6,7,8]
c = a + b

print(c)
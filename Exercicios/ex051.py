print('-=' * 15)
print('\t10 TERMOS DE UMA PA')
print('-=' * 15)

n1 = int(input('Primeiro termo:'))
r = int(input('Razão:'))

for contador in range(n1,10* r,r):
    print(contador)


print('-=' * 15)
print('\t10 TERMOS DE UMA PA')
print('-=' * 15)

n1 = int(input('Primeiro termo:'))
r = int(input('Razão:'))
d = n1 + (10-1) * r

for contador in range(n1,d + r,r):
    print(contador, end=' ')


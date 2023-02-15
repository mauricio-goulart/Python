#num = [1 , 2, 3]
#num[2] = 999
#num.append(7)
#num.sort()
#num.insert(2,4)
#print(num)
jogos = ['Hogwarts Legacy', 'The Witcher 3', 'Cyberpunk 2077', 'Skyrim']

for pos,jogo in enumerate(jogos):
    print(f'Na posição {pos + 1} = {jogo}')

print('Fim da lista')



a = [1,2,3,4]
b = a[:]
b[2] = 8

print(f'LISTA A :{a}')
print(f'LISTA B :{b}')
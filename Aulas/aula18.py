pessoas = [['Mauricio',18],['Maria',16]]
print(pessoas[1])

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')



galera = list()
dado = list()

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
jogador = dict()
gols = list()
tot = 0
totg = 0
print('-=' * 14)
jogador['Nome'] = str(input('Nome do Jogador: '))
jogos = int(input(f'Quantos partidas {jogador["Nome"]} jogou: '))
for c in range(1, jogos + 1):
    tot = int(input(f'Gols na partida [{c}]: '))
    gols.append(tot)
    totg = tot + totg

jogador['Total'] = totg
jogador['Gols'] = gols
print('-=' * 15)

for k,v in jogador.items():
    print(f'{k} = {v}')
print('-=' * 15)
print(f'O jogador {jogador["Nome"]} jogous {jogos} partidas.')
for i,g in enumerate(gols):
    print(f'--> Partida {i} fez {g} gols')
print('-=' * 15)

def ficha(jogador = '', gols = 0):
    if jogador == '':
        print('Jogador: <desconhecido>')
        print(f'Gols: {gols}')
    elif gols == 0:
        print(f'Jogador: {jogador}')
        print(f'Gols: 0')
    elif jogador == '' and gols == 0:
        print(f'Jogador: <desconhecido>')
        print(f'Gols: 0')
    else:
        print(f'Jogador: {jogador}')
        print(f'Gols: {gols}')


print('-=' * 15)
nome = str(input('Nome do Jogador: '))
gols = int(input('Gols: '))
print('-=' * 15)
ficha(nome,gols)
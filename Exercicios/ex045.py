from random import randint
itens = ('Pedra' , 'Papel', 'Tesoura')
computador = randint(0,2)

print(f'{"JOKENPO":=^20}')
print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')
jogador = int(input('Sua jogada: '))

print('-=' * 10)
print(itens[jogador])
print(itens[computador])

if computador == 0: #pc pedra
    if jogador == 1:
        print('Jogador Ganhou')
    elif jogador == 2:
        print('Jogador Perdeu')
    elif jogador == 0:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')

elif computador == 1: #pc papel
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador Ganhou')
    elif jogador == 0:
        print('Jogador Perdeu')

elif computador == 2:
    if jogador == 1:
        print('Jogador Perdeu')
    elif jogador == 2:
        print('EMPATE')
    elif jogador == 0:
        print('Jogador Ganhou')
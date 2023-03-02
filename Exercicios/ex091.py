from random import randint
from operator import itemgetter
jogo = {"jogador1":randint(1,6),
        "jogador2":randint(1,6),
        "jogador3":randint(1,6),
        "jogador4":randint(1,6)}
rank = dict()
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(rank)
print('-=' * 15)
print('\tValores Sorteados')
print('-=' * 15)

for k,v in jogo.items():
    print(f'{k} = {v}')
print('-=' * 15)
for i, v in enumerate(rank):
    print(f'{i+1}ºLugar = {v[0]} : {v[1]}')

from random import randint

v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = computador + jogador
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar: [P/I]')).strip().upper()
    print(f'Você:[{jogador}]')
    print(f'Computador:[{computador}]')
    print(f'Total:[{total}]')
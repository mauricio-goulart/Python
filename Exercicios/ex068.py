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
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce, VENCEU!!')
            v = v + 1
        else:
            print('Voce, PERDEU!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce, GANHOU!!')
            v = v + 1
        else:
            print('Voce, PERDEU!!')
            break
            
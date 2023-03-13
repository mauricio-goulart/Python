def LeiaInt(n):
    n1 = str(n)
    while True:
        try:
            if n1.isnumeric():
                nv = int(n1)
        except:
            nv = int(input('Digite um numero certo: '))
        else:
            break








print(f'Digitou : {LeiaInt(n)}')
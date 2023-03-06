def inp(n):
    ok = False
    valor = 0
    while True:
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('DIGITE UM NUMERO VALIDO')
            n = input('Digite: ')
        if ok:
            break
    return valor





n = input('Digite um valor:')
print(f'Digitou : {inp(n)}')
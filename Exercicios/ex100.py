from random import randint
print('-=' * 15)


def sorte(list):
    print('Os valores sorteados: ')
    par = 0
    for n in list:
        print(n, end=' ')
        if n % 2 == 0:
            par = par + n
    print(f'\nSoma par: {par}')




valores = [randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),randint(1,5),]
sorte(valores)
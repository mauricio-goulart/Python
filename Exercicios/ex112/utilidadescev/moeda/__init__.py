def metade(n, f = False):
    m = n /2
    if f:
        return f'R${m}'.replace('.',',')
    return m


def dobro(n, f = False):
    m = n * 2
    if f:
        return f'R${m}'.replace('.',',')
    return m


def triplo(n, f = False):
    m = n * 3
    if f:
        return f'R${m}'.replace('.',',')
    return m


def aumenta(n=0, p=0, f = False):
    m = (n * p) / 100 + n
    if f:
        return f'R${m}'.replace('.',',')
    return m


def retira(n=0 , p=0, f = False):
    m = n - (n * p) / 100
    if f:
        return f'R${m}'.replace('.',',')
    return m


def moeda(n=0, p='R$'):
    return f'{p}{n}'.replace('.',',')


def resumo(n = 0, ta = 10, tr = 10):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Valor analisado: \t\t{moeda(n)}')
    print(f'Dobro do valor: \t\t{dobro(n,True)}')
    print(f'Triplo do valor: \t\t{triplo(n, True)}')
    print(f'Com {ta}% de aumento: \t{aumenta(n,ta,True)}')
    print(f'Com {tr}% de reducao: \t{retira(n,tr,True)}')
    print('-' * 30)
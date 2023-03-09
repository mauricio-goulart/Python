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

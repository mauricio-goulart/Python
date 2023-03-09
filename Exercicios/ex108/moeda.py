def metade(n):
    m = n /2
    return m


def dobro(n):
    m = n * 2
    return m


def triplo(n):
    m = n * 3
    return m


def aumenta(n=0, p=0):
    m = (n * p) / 100 + n
    return m


def retira(n=0 , p=0):
    m = n - (n * p) / 100
    return m


def moeda(n=0, p='R$'):
    return f'{p}{n}'.replace('.',',')

def contar(i, f, p):
    """
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passos da contagem
    :return: 
    """

    c = 0
    while c <= f:
        print(c, end=" ")
        c = c + p


help(contar)

contar(1, 10, 2)


def somar(a = 0,b = 0, c = 0):
    s = a + b + c
    print(s)


somar(10,2,5)
somar(4,7)



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
    return s


r1 = somar(10,2,5)
r2 = somar(4,7)

print(f'A soma deu {r1} ')


def par(n = 0):
    if n % 2 ==0:
        return True
    else:
        return False


n = int(input('Digite um numero: '))
r = par(n)

if r :
    print('Par')
else:
    print('Impar')



def fatorial(num):
    f = 1
    for c in range(1, num+1):
        f = f * c

    return f

def dobro(n):
    return n * 2



def triplo(n):
    return n *3


n = int(input('Digite um valor: '))
print(f'FATORIAL: {fatorial(n)}\nDOBRO: {dobro(n)}\nTRIPLO: {triplo(n)}')
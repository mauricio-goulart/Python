def titulo(txt):
    print('-=' * 30)
    print(f'\t{txt}')
    print('-=' * 30)



titulo('PREENDA-ME SE FOR CAPAZ')

def soma(a,b):
    s = a + b
    print(s)


soma(4,5)
soma(b = 5, a = 4)


def somar(*valores):
    s = 0
    for num in valores:
        s = s + num
    print(f'Somando  {valores} = {num}')


somar(5,6,5,6)





def dobrar(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos = pos + 1


valores = [2,3,4]
dobrar(valores)
print(valores)
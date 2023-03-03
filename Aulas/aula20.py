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

def contador(*num):

    print(f'Recebi os valores {num} e tem {len(num)} numeros')


contador(5,3,1,4)
contador(4,2,1)
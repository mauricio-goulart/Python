from time import sleep

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
sair = False
d = ''
print('-=' * 15)
while not sair:
    print('\t[ 1 ] Somar')
    print('\t[ 2 ] Multiplicar')
    print('\t[ 3 ] Maior')
    print('\t[ 4 ] Novos números')
    print('\t[ 5 ] Sair do programa')
    d = str(input('>>>> Qual a sua opção: ')).strip()
    if d == '1':
        print('-=' * 15)
        print(f'\t[{n1}] + [{n2}] = [{n1 + n2}]')
        print('-=' * 15)
        sleep(1)
    elif d == '2':
        print('-=' * 15)
        print(f'\t[{n1}] x [{n2}] = [{n1 * n2}]')
        print('-=' * 15)
        sleep(1)
    elif d == '3':
        if n1 > n2:
            print('-=' * 15)
            print(f'\tMaior número:[{n1}]')
            print('-=' * 15)
            sleep(1)
        else:



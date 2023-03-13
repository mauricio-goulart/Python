def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('-=' * 15)
            print('\033[31mERRO: NUMERO INVALIDO\033[m')
            continue
        else:
            return n






print('-=' * 15)
num = LeiaInt('Digite um valor: ')
print('-=' * 15)
print(f'\033[32mO valor digitado foi {num}\033[m')









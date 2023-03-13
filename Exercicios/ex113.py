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



def LeiaFloat(msg):
    while True:
        try:
            f = float(input(msg))
        except:
            print('-=' * 15)
            print('\033[31mERRO: NUMERO INVALIDO\033[m')
            continue
        else:
            return f





print('-=' * 15)
num = LeiaInt('Digite um valor inteiro: ')
float = LeiaFloat('Digite um valor real: ')
print('-=' * 15)
print(f'\033[32mO valor digitado foi {num} e {float}\033[m')









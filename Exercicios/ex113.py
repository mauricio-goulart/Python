def LeiaInt(msg):
    while True:
        try:
            n = int(input('Digite um numero:'))
        except:
            print('Digite um numero certo')
            continue
        else:
            return n


num = LeiaInt('Digite um valor: ')
print(f'O valor digitado foi {num}')









try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    c = a/b
    print('-=' * 15)
except:
    print('-=' * 15)
    print('Tivemos um problema!')

else:
    print(f'{c}')
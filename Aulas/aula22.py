try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    c = a/b
except:
    print('Tivemos um problema!')

else:
    print(f'{c}')
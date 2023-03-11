try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    c = a/b
    print('-=' * 15)
except ZeroDivisionError:
    print('-=' * 15)
    print('Tivemos um problema! Não se divide algo por 0 !')
except (ValueError, TypeError):
    print('-=' * 15)
    print('Tivemos um problema! Digite um valor valido!')
except KeyboardInterrupt:
    print('-=' * 15)
    print('Tivemos um problema! Vc abandonou o programa')
else:
    print(f'{c}')

finally:
    print('Volte sempre')
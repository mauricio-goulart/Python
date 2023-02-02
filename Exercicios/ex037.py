n1 = int(input('Digite um número: '))
print('=' * 20)
print('Escolha uma opção:')
print('[ 1 ] Converter em Hexadecimal')
print('[ 2 ] Converter em Binário')
print('[ 3 ] Converter em Octal')
o = str(input('Opção:')).strip()



if o == '1':
    print(f'{n1} to Hexadecimal:[{hex(n1)}]')
elif o == '2':
    print(f'{n1} to Binário:[{bin(n1)}]')
elif o == '3':
    print(f'{n1} to Octal:[{oct(n1)}]')

print('=' * 20)
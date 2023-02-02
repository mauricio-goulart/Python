print(f'{"-=" * 5}{"LOJA MAURICIO"}{"=-" * 5}')
p = float(input('Preço das compras: '))
print('-=' * 16)

print('[ 1 ] Débito')
print('[ 2 ] Crédito')
print('[ 3 ] 2x Crédito')
print('[ 4 ] 3x Crédito ou mais')

d = input('Forma de Pagamento: ').strip()
print('-=' * 16)

if d == '1':
    print(f'[R${p}] --> [R${p - (p * 10) / 100:.2f}]')
elif d == '2':
    print(f'[R${p}] --> [R${p - (p * 5) / 100:.2f}]')
elif d == '3':
    print(f'[R${p}]')
elif d == '4':
    pp = int(input('Quantas parcelas: '))
    print(f'R${p} --> [{pp}x de { (p/10) + (p * 20) /100 /pp }] --> [R${p + (p * 20) / 100:.2f}]')
print('-=' * 16)

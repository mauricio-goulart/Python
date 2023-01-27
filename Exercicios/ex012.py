n1 = float(input('Preço:'))
des = (n1*5)/100

print(f'{"Desconto":=^20}')
print(f'Preço: [R${n1}]')
print(f'Preço com Desconto: [R${n1 - des:.2f}]')
print(20 * '=')
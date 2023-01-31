sala = float(input('Digite seu salário: R$'))
print(f'{"Reajuste":=^20}')
if sala > 1200 :
    print(f'Salario reajustado:[R${(sala * 15 / 100) + sala}]')
else:
    print(f'Salário reajustado:[R${(sala * 15 / 100) + sala}]')
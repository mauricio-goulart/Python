kg = float(input('Digite o seu peso (Kg):'))
al = float(input('Digite a sua altura (m):'))
imc = kg / (al**2)
print('-=' * 15)
if imc < 18.5 :
    print(f'IMC:[{imc:.1f}]')
    print('[Abaixo do Peso]')
elif imc >= 18.5 and imc <26 :
    print(f'IMC:[{imc:.1f}]')
    print('[Ideal]')
elif imc >= 25 and imc < 31 :
    print(f'IMC:[{imc:.1f}]')
    print(f'[Sobrepeso]')
elif imc >= 30 and imc < 41 :
    print(f'IMC:[{imc:.1f}]')
    print(f'[Obesidade]')
elif imc > 40 :
    print(f'IMC:[{imc:.1f}]')
    print(f'[Obesidade Morbida]')

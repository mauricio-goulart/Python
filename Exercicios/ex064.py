
cont = 0
soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    cont = cont + 1
    soma = soma + n
    n = int(input('Digite um número [999 para parar]: '))

print('-=' * 15)
print(f'Você digitou [{cont}] vezes e a soma entre eles são [{soma}]')
print('-=' * 15)

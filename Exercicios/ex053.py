p = str(input('Digite algo: ')).strip().upper()
print('-=' * 15)
separad = p.split()
junto = ''.join(separad)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]


print(inverso, end=' ')
if p == inverso:
    print('| Palindromo:[SIM]')
else:
    print('| Palindromo:[NÃO]')
print('-=' * 15)
sexo = str(input('Digite o seu sexo: [M/F]')).upper().strip()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados Invalidos, Digite um sexo valido: [M/F]')).upper().strip()

print(f'Sexo {sexo} registrado com sucesso!')
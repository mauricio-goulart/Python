sexo = str(input('Digite o seu sexo: [M/F]')).upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados Invalidos, Digite um sexo valido: [M/F]')).upper()

print(f'Sexo {sexo} registrado com sucesso!')
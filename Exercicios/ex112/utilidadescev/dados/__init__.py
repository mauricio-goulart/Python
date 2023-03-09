def validar(n):
    valido = False
    while not valido:
        entrada = str(input(n)).replace('.',',')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO: {entrada} não é valido!')
        else:
            valido = True
            return float(entrada)
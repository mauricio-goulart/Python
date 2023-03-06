def titulo(txt, cort = 31, corf = 45, x = 0):
    """
    função dedicada à imprimir textos com cores de texto e de fundo personalizadas

    :param txt: recebe o texto que vai aparecer
    :param cort: seleciona a cor do texto
    :param corf: seleciona a cor de fundo
    :param x: seleciona o espaço em que a frase vai ser escrita
        caso x seja 0, ou seja, o padrão, vai receber o len de txt + 6 espaços
    :return: sem retorno
    """
    if x == 0:
        x = len(txt) + 6
    print(f'\033[1;{cort};{corf}m', end='')
    print('~' * x)
    print(F'{txt:^{x}}')
    if txt == 'SISTEMA DE AJUDA PyHELP':
        print(f'{"(digite fim para finalizar)":^{x}}')
    print('~' * x)
    print('\033[m', end='')


def fun(txt):
    """
    função dedicada à mostrar o help de cada função do python

    :param txt: seleciona a função que vai ser pesquisada
    :return: sem retorno
        obs* esta sendo utilizado em conjunto com a função 'titulo'
    """
    x = len(txt) + 36
    titulo(f"Acessando o manual do comando {txt}", 31, 44, x)

    print('\033[1;7;40m', end='')
    print(f"{help(txt)}")
    print('\033[m', end='')



# PROGRAMA PRINCIPAL:
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    função = str(input('Função ou bilbioteca > ')).lower().strip()
    if função == 'fim':
        titulo(txt = 'PROGRAMA FINALIZADO!', corf=43)
        break
    fun(função)
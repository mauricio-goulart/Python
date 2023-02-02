from time import sleep
cont = int(0)
print('-=' * 15)
m = int(input('Digite o número: '))
print('-=' * 15)


for contador in range(0,11):
    print(f'{m} x {cont} = {m*cont}')
    cont = cont + 1
    sleep(0.5)
print('-=' * 15)
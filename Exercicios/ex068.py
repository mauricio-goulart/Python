from random import randint
from time import sleep
impar = 0
par = 0
print('=-' * 15)
print('\tÍMPAR OU PAR')
print('=-' * 15)
pc = randint(0, 10)
h = int(input('Digite um valor: '))
dec = input('Impar ou Par:[I/P]')
print('=-' * 15)
conta = (pc + h) % 2

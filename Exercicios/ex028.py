import random
import time

print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)

pc = int(random.randint(0, 5))
h = int(input('Em que número eu pensei? :'))
print('PROCESSANDO...')
time.sleep(2)

if h == pc :
    print(f'Parabens!!! Você ganhou eu pensei no {pc}')
else:
    print(f'Perdeu!!! Você errou eu pensei no {pc}')
print('=' * 40)

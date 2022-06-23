from random import randint
from time import sleep
computador = randint(0,5)
print('--' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('--' * 30)
jogador = int(input('Em que número pensei?'))
print('Processando ....')
sleep(2)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!!')

else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))
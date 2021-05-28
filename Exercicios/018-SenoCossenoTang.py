print('=====Desafio 018=====')
#import math
from math import radians, sin, cos, tan
ang=float(input('Digite o ângulo que você deseja: '))
seno= sin(radians(ang))
cos= cos(radians(ang))
tan= tan(radians(ang))


print('O ângulo de {} tem:\nSENO de {:.2f}\nCOSSENO de {:.2f}\nTANGENTE de {:.2f}'.format(ang, seno, cos, tan))
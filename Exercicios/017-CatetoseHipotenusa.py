print('=====Desafio 017=====')

'''opo=float(input('Comprimento do cateto oposto: '))
adj=float(input('Comprimento do cateto adjacente '))
hi= (opo **2 + adj **2) **(1/2)

print('A soma dos quadrados {} e {} é igual ao quadrado da hipotenusa {:.2f}'.format(opo, adj, hi))'''

from math import hypot
opo=float(input('Comprimento do cateto oposto: '))
adj=float(input('Comprimento do cateto adjacente '))
hi = hypot(opo, adj)

print('A soma dos quadrados {} e {} é igual ao quadrado da hipotenusa {:.2f}'.format(opo, adj, hi))
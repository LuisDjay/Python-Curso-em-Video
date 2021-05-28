print('=====Desafio 034=====')

a=int(input('Primeiro Valor: '))
b=int(input('segundo Valor: '))
c=int(input('Terceiro Valor: '))

#verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificando quem é maior
maior = a
if b>a and b>c:
    menor = b
if c>a and c>b:
    menor = c

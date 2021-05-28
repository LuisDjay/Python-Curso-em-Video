print('=====Desafio 031=====')

dist=int(input('Qual a distância da viagem? '))


print('Você está prestes a iniciar uma viagem de {:.1f}Km'.format(dist))

if dist >= 200:
   valor= dist*0.45
else:
    valor= dist*0.50

print ('E o preço da sua passagem será de R${:.2f}'.format(valor))
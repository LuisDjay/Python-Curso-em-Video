print('=====Desafio 015=====')

dia=int(input('Quantos dias alugados? '))
km= float(input('Quantos Km rodados? '))
pago =float(60.00*dia) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(pago))



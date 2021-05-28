print('=====Desafio 010=====')
real =float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.62
yen = real / 0.053
euro = real / 6.78
print('Com R${:.2f}, você pode comprar U${:.2f}, EU {:.2f}, Y {:.2f} '.format(real, dolar, euro, yen))


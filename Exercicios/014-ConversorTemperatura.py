print('=====Desafio 014=====')

temp=float(input('Informe a Temperatura em °C: '))
f = temp * 1.8 + 32
k = temp * 273.15 + temp

print ( ' A temperatura de {}°C corresponde a {:.1f}°F e {:.1F}°K'.format(temp, f, k,))

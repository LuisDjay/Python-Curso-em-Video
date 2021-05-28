print('=====Desafio 029=====')

v1 = int(input('Qual a velocidade atual do carro? '))
m = (v1 - 80) * 7
if v1 < 81:
    print('Tenha um bom dia, dirija com segurança')
else:
    print('MULTADO! Você excedeu o limite permitido que é 80Km/h\nVocê deve pagar uma multa de R${:.2f}!'.format(m))
    print('Tenha um bom dia! Dirija com segurança!')

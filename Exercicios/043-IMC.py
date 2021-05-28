print('=====Desafio 043=====')

peso = float(input('Qual o seu peso? (Kg)'))
alt = float(input('Qual a sua altura? (M)'))
imc = peso / (alt **2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5 :
    print('Você está ABAIXO DO PESO normal')
elif imc <= 25:
    print('Você está no PESO ideal')
elif imc <=30 :
    print('Você está ACIMA DO PESO normal')
elif imc <= 40:
    print('Você está em OBESIDADE, cuidado')
elif imc > 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')


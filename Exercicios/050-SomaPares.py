print('=====Desafio 050=====')
soma = 0
for c in range (1,7):
    num= int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0: # == verifica se a divisao é igual a zero
        soma += num
print('A soma entre os numeros é {}'.format(soma))




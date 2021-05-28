print('=====Desafio 027=====')

n=str(input('Digite seu nome completo: ')).strip()
nome=n.split()
print('Analisando os dados.....')
print('Muito prazer em te conhecer! ')
print('Seu primeiro nome é {} '.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))


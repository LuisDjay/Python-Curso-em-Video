print('=====Desafio 012=====')

preco=float(input('Qual o preço do produto? R$'))
novo= preco - (preco * 5 /100)
#desconto = produto*0.05
#valor = produto-desconto

print( 'O produto que vale {:.2f}  está saindo por {:.2f}  '.format(preco, novo))

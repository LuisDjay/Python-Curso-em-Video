from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não possui): '))
if dados['ctps'] !=0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salario R$: '))
    dados[ 'Aposentadoria'] = dados['idade'] + ((dados['Contratação'] + 35)) - datetime.now().year
print('=*'*30)
for k, v in dados.items():
    print(f' -{k} tem o valor {v}')

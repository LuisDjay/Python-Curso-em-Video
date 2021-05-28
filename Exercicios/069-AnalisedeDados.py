
def linhas():
    print('='*30)
print('CADASTRE UMA PESSOA')
tot18 = masc = fem20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper()[0].strip()
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        fem20 += 1
    resp= ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?  [S/N]')).upper()[0].strip()
    linhas()
    if resp == 'N':
        break
print(f'O total de pessoas maiores de 18 anos é {tot18}')
print(f'O total de pessoas do sexo masculino é {masc}')
print(f'O total de mulheres menores de 20 anos é {fem20}')
linhas()
print('Acabou')
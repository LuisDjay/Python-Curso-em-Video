print('-----Desafio 066-----')
soma = cont = 0
while True:
    n1 = int(input('Digite um valor (999 para parar): '))
    if n1 == 999:
        break
    cont += 1 # nao conta o Flag
    soma += n1  # soma recebe soma (ele mesmo ) + n1
print(f'A soma dos {cont} valores foi {soma}!')
print('Acabou')


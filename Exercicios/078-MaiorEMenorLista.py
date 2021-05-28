""""valores = []
for cont in range(0,5):
        valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
for c, v in enumerate(valores):
    print(f'', end=' ')
print(f'O Maior valor digitado foi {max(valores)}, na posiçao {c}')
print(f'O Menor valor digitado foi {min(valores)}, na posiçao {c}')
print('=-' *30)
print(f'Você digitou os valores {valores}')"""

listanum= []
mai = 0
men = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men =listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
            if listanum[c] < men:
                men = listanum[c]
print('=-' *30)
print(f'Você digitou os vslores {listanum}')
print(f'O Maior valor digitado foi {mai}, nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ',end='')
print()
print(f'O Menor valor digitado foi {men}, nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ',end='')
print()

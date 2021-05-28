time = list()
jogador = dict()
partidas = list()
def lin():
    print('=*' * 40)
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} Jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'  Quantos gols na partida {c+1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N. ')
    if resp == 'N':
        break
lin()
print('cod ', end= ' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
lin()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
lin()
while True:
    busca = int(input('Mostrar os dados de qual jogador? ( 999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com codigo {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca][ 'gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    lin()
print('<<< VOLTE SEMPRE >>>')



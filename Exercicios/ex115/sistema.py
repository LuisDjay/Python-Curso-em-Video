from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta ==1:
        #Opcao de listar o conteudo do arquivo
        lerArquivo(arq)
    elif resposta ==2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema.... Até Logo!')
    else:
        print('\033[31m Erro! Digite uma opção válida!\033[m')
    sleep(1)
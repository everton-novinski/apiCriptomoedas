from time import sleep
import requests


def main():
    sleep(1)
    print('=' * 32)
    print('''Escolha uma destas criptomoedas:
    CARDANO(ADA)
    BITCOIN(BTC)
    ETHEREUM(ETH)
    SOLANA(SOL)
    AVALANCHE(AVAX)
    CHAINLINK(LINK)''')
    print('=' * 32)

    moeda = input('Qual criptomoeda você deseja consultar? ').upper()
    sleep(1)

    if moeda == 'CARDANO' or moeda == 'ADA':
        cripto = 'CARDANO(ADA)'
        print(f'A criptomoeda escolhida foi: \033[31;40m{cripto}\033[m.')
        print('Processando os valores...')
        resposta = requests.get(
            'https://www.mercadobitcoin.net/api/ADA/ticker/')

        dados = resposta.json()

        valor_moeda = float(dados['ticker']['sell'])
        open = float(dados['ticker']['open'])
        

    elif moeda == 'BITCOIN' or moeda == 'BTC':
        cripto = 'BITCOIN(BTC)'
        print(f'A criptomoeda escolhida foi: \033[31;40m{cripto}\033[m.')
        print('Processando os valores...')

        resposta = requests.get(
            'https://www.mercadobitcoin.net/api/BTC/ticker/')

        dados = resposta.json()

        valor_moeda = float(dados['ticker']['sell'])
        open = float(dados['ticker']['open'])
        

    elif moeda == 'ETHEREUM' or moeda == 'ETH':
        cripto = 'ETHETEUM(ETH)'
        print(f'A criptomoeda escolhida foi: \033[31;40m{cripto}\033[m.')
        print('Processando os valores...')

        resposta = requests.get(
            'https://www.mercadobitcoin.net/api/ETH/ticker/')

        dados = resposta.json()

        valor_moeda = float(dados['ticker']['sell'])
        open = float(dados['ticker']['open'])
        

    elif moeda == 'SOLANA' or moeda == 'SOL':
        cripto = 'SOLANA(SOL)'
        print(f'a criptomoeda escolhida foi: \033[31;40m{cripto}\033[m.')
        print('Processando os valores...')

        resposta = requests.get(
            'https://www.mercadobitcoin.net/api/SOL/ticker/')

        dados = resposta.json()

        valor_moeda = float(dados['ticker']['sell'])
        open = float(dados['ticker']['open'])
        

    elif moeda == 'AVALANCHE' or moeda == 'AVAX':
        cripto = 'AVALANCHE(AVAX)'
        print(f'A criptomoeda escolhida foi: \033[31;40m{cripto}\033[m.')
        print('Processando os valores...')

        resposta = requests.get(
            'https://www.mercadobitcoin.net/api/AVAX/ticker/')

        dados = resposta.json()

        valor_moeda = float(dados['ticker']['sell'])
        open = float(dados['ticker']['open'])
        

    elif moeda == 'CHAINLINK' or moeda == 'LINK':
        cripto = 'CHAINLINK(LINK)'
        print(f'A criptomoeda escolhida foi: \033[31;40m{cripto}\033[m.')
        print('Processando os valores...')

        resposta = requests.get(
            'https://www.mercadobitcoin.net/api/LINK/ticker/')

        dados = resposta.json()

        valor_moeda = float(dados['ticker']['sell'])
        open = float(dados['ticker']['open'])

    sleep(2)
    try:
        print(f'O valor da criptomoeda é de R${valor_moeda:.2f} no momento.')
        sleep(1)
        print(f'A criptomoeda abriu com  valor de R${open:.2f}.')
        sleep(1)

    except NameError:
        print('\033[31;40mCriptomoeda invalida \033[m, somente criptomoedas do menu.')

def nova_consulta(resp):
   
    if resp == 'SIM' or resp == '1':
        sleep(1)
        main()
        nova_consulta(input( 'Você deseja consultar outra criptomoeda? \n1. Sim\n2. Sair\n').upper())

    elif resp == 'SAIR' or resp == '2':
        sleep(1)
        print('Saindo... Obrigado.')
    else:
        print('Opcão invalida.')
        nova_consulta(input( 'Você deseja consultar outra criptomoeda? \n1. Sim\n2. Sair\n').upper())
                
        


if __name__ == '__main__':
    main()

nova_consulta(input( 'Você deseja consultar outra criptomoeda? \n1. Sim\n2. Sair\n').upper()) 
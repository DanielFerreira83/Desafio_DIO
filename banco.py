''' REGRA
CRIAR UM SISTEMA BANCÁRIO COM AS OPERAÇÕES: DEPOSITAR, SACAR  E VISUALIZAR EXTRATO.
SÓ É PERMITIDO REALIZAR 3 SAQUES NO VALOR DE R$ 500, CADA.
TODOS OS DEPOSITOS DEVEM SER ARMAZENADOS EM UMA VARIÁVEL E EXIBIDOS NO EXTRATO.
OS VALORES DEVEM SER EXIBIDOS FORMATADOS
'''

menu = '''\nMeu Banco
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
'''
valor_max = 500
saque_max = 3
extrato = ""
saldo = 0

while True:
    op = input(menu)
   
    if op == 'd':
        valor = float(input('Valor depositado: '))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print('Valor de deposito inválido!\n')

    elif op == 's':
        if saque_max > 0:
            valor = float(input('Valor de saque: '))

            if saldo < valor:
                print('Saldo indisponível para saque.')


            elif (valor > 0 and valor <= valor_max):
                saldo -= valor
                extrato += f'Saque: R$ {valor:.2f}\n' 
                
                saque_max -= 1

            else:
                print(f'Valor limite de saque excedido. Limite máximo R$ {valor_max:.2f}\n')

        else:
            print('Limite de saque excedido!')


    elif op == 'e':
        print(f'\nEXTRATO')
        print('=' * 20)
        print('Sem movimentação' if not extrato else extrato)

        print('-' * 20)
        print(f'Saldo: R$ {saldo:.2f}')
        print('=' * 20)

    elif op == 'q':
        break

    else:
        print('Opção inexitente!')

print('fim do acesso...')

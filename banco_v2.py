
def menu():
    menu = """
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tSair
    => """
    return int(input(menu))


def depositar(saldo, valor, extrato):
    saldo += valor
    extrato += f"Depósito: {valor:.2f}\n"
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    com_saldo = saldo >= valor
    saque = numero_saques <= limite_saques
    valor_liberado = valor <= limite

    if not com_saldo:
        print('Valor não disponível para saque!!\n')
    elif not saque:
        print('Limite de saque excedido!\n')
    elif not valor_liberado:
        print('Valor excede limite de saque!\n')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: {valor:.2f}\n'
        # Não consegui resolver esse problema ( somar numero de saques )
        numero_saques += 1
        print(f'qtd saques - > {numero_saques}')

    else:
        print('Operação falhou!!')

    return saldo, extrato


def exibe_extrato(saldo, /, *, extrato):
    print('Extrato'.center(40))
    print('-' * 40)
    print(f'Sem movimentação!\n' if not extrato else extrato)
    print(f'Saldo: {saldo:.2f}\n')


def nova_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o cpf: ')
    usuario = filtra_usuario(cpf, usuarios)

    if usuario:
        print('----> Conta criada !')
        return {'agencia': agencia, 'conta': numero_conta, 'usuario': usuario}


def listar_conta(contas):
    for conta in contas:
        print(f'''
            Agencia: {conta['agencia']}
            Conta: {conta['conta']}
            Usiário: {conta['usuario']['nome']}
''')
    if not contas:
        print('Sem contas cadastradas !!')


def filtra_usuario(cpf, usuarios):
    usuario_filtrado = [
        usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None


def criar_usuario(usuarios):  # nome. data de nasciemnto, spf, enredeço / chave - valar
    cpf = input('CPF: ')
    usuario = filtra_usuario(cpf, usuarios)

    if usuario:
        print('Já existe usuário com esse cpf!')
    else:
        nome = input("Nome: ")
        endereco = input('Endereço: ')
        d_nasc = input('Data de nascimento: ')

        usuarios.append({'nome': nome, 'd_nasc': d_nasc,
                         'cpf': cpf, 'endereco': endereco})

        print('------> Usuário criado com sucesso !')


def main():

    AGENCIA = '0001'
    LIMITE_SAQUE = 3

    numero_conta = 0
    saldo = 0
    limite = 500
    numero_saques = 0

    extrato = ""
    usuarios = []
    contas = []

    while True:
        op = menu()

        if op == 1:
            valor = float(input('Valor do depósito: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif op == 2:
            valor = float(input('Valor de saque: '))
            saldo, extrato = sacar(saldo=saldo,
                                   valor=valor,
                                   extrato=extrato,
                                   limite=limite,
                                   numero_saques=numero_saques,
                                   limite_saques=LIMITE_SAQUE)

        elif op == 3:
            exibe_extrato(saldo, extrato=extrato)

        elif op == 4:
            numero_conta += 1
            contas.append(nova_conta(AGENCIA, numero_conta, usuarios))

        elif op == 5:
            listar_conta(contas)

        elif op == 6:
            criar_usuario(usuarios)

        elif op == 7:
            break


main()

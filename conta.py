import clientes as fc
def criar_conta(AGENCIA, contas, clientes, saldo, extrato):
    cpf = input('Informe o seu cpf(somente numeros): ')
    cliente = fc.verificar_cliente_cpf(clientes, cpf)
    if cliente:
        numero_conta  = len(contas)+1    
        contas.append({'agencia': AGENCIA, 'numero_conta': numero_conta, 'saldo': saldo,'extrato': extrato, 'cliente': cliente})
        print('Conta criada com sucesso!')
    else:
        print('Cliente não cadastrado!!')


#verificar se o cpf está cadastrado em alguma conta
def verificar_conta_cpf(contas, cpf):
    for conta in contas:
        if conta['cliente']['cpf'] == cpf:
            return conta
    return None

#lista todas as contas cadastradas
def listar_contas(contas):
    for conta in contas:
        print(conta)


#imprime as informações de uma conta
def consultar_conta(contas):
    num_conta = int(input('Informe o numero da conta: '))
            
    conta = verifica_numero_conta(contas, num_conta)
    if conta:
        print(conta)
    else:
        print('Conta não existente!\n')
 
#verifica se existe uma conta com o numero informado pelo usuário
def verifica_numero_conta(contas, num_conta):
    for conta in contas:
        if conta['numero_conta'] == num_conta:
            return conta
    return None

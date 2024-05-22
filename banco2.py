from random import randint as rd

def menu():
    print('\n=============================================')
    print('Informe o que deseja fazer:')
    print('1 - Depositar\n2 - Sacar\n3 - Extrato\n4 - Cadastrar cliente\n5 - Criar conta\n6 - Sair')
    print('=============================================\n')
    return int(input('= '))

#def criar_usuario(usuarios):
    

def depositar(valor, conta):
    if valor > 0:
        conta['saldo'] += valor
        conta['extrato'] += f'Deposito de: {valor:.2f}\n'
                
    else:
        print('Operação falhou, tente novamente!!\n')
    return conta

def sacar(valor, saldo, extrato, numero_saques, LIMITE_SAQUES, limite):
    saque_excedido = numero_saques >= LIMITE_SAQUES
    if saque_excedido == False:
        valor = float(input('Informe o valor que deseja sacar: '))
        
        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
                
        if saldo_excedido: 
            print('Operação inválida! Saldo insuficiente!\n ')
        elif limite_excedido:
            print('Operação inválida! Excedeu o limite de saque!\n ')   
        else:
            saldo-=valor
            extrato+= f'Saque de {valor:.2f}\n'
            numero_saques+=1 
    else:
        print('Operação inválida! O numero de saques permitidos foi excedido!\n ')

    return saldo, extrato, numero_saques
 
def imprimir_extrato(extrato, saldo):
    print(extrato)
    print(f'Saldo total: {saldo:.2f}')

def cadastrar_cliente(clientes):
    cpf = input('Informe o seu cpf: ')
    
    for i in clientes:
        if i['cpf'] == cpf:
            return
        
    nome = input('Informe o seu nome: ')
    
    clientes.append({"nome": nome, "cpf": cpf})

def gerar_numero():
    return rd(100000000, 9999999999)

def criar_conta(AGENCIA, contas, clientes, saldo):
    cpf = input('Informe o seu cpf: ')
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            numero_conta  = gerar_numero()
            contas.append({'agencia': AGENCIA, 'numero_conta': numero_conta, 'cliente': cliente, 'saldo': saldo})

      
def main(): 
    clientes = []
    contas = []
    extrato = ''
    limite = 1000
    numero_saques = 0
    LIMITE_SAQUES = 5
    saldo = 0
    AGENCIA = '0001'
    
    while True:   
        op = menu()
        
        if op == 1:
            print('\n---------------------------------------------\n')
            cpf = input('Informe o seu cpf: ')
            for conta in contas:
                if conta['cliente']['cpf']== cpf:
                    valor = float(input('Informe o valor que deseja depositar: '))
                    contas = depositar(valor, contas)
                    
                else:
                    print('Crie primeiro uma conta!\n')
                    
            print('\n---------------------------------------------\n')
        elif op == 2:
            print('\n---------------------------------------------\n')
            saldo, extrato, numero_saques = sacar(valor, saldo, extrato, numero_saques, LIMITE_SAQUES, limite)
            print('\n---------------------------------------------\n')
        elif op == 3:
            print('\n-------------------EXTRATO-------------------\n')
            imprimir_extrato(extrato, saldo)
            print('\n---------------------------------------------\n')
        elif op == 4:
            cadastrar_cliente(clientes)
            print(clientes)
            
        elif op == 5:
            criar_conta(AGENCIA, contas, clientes, saldo)
            print(contas)
        elif op == 6:
            print('Programa encerrado...\n ')
            break
        else:
            print('Opção inválida!!\n')

main()
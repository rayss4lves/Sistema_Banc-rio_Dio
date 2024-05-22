from random import randint as rd

def menu():
    print('\n=============================================')
    print('Informe o que deseja fazer:')
    print('1 - Depositar\n2 - Sacar\n3 - Extrato\n4 - Cadastrar cliente\n5 - Criar conta\n6 - consultar conta\n7 - consultar cliente\n8 - Sair')
    print('=============================================\n')
    return int(input('= '))
    

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito de: {valor:.2f}\n'
               
    else:
        print('Operação falhou, tente novamente!!\n')
    return saldo, extrato


#função para sacar o valor
def sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite):
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
 

def imprimir_extrato(contas):
    cpf = input('Informe o seu cpf: ')
    
    for conta in contas:
        if conta['cpf'] == cpf:
            print('\n-------------------EXTRATO-------------------\n')
            print(conta['extrato'])
            print('\n---------------------------------------------\n')
        else:
            print('Conta não encontrada!!')
def cadastrar_cliente(clientes):
    cpf = input('Informe o seu cpf: ')
    
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            return
        
    nome = input('Informe o seu nome: ')
    
    clientes.append({"nome": nome, "cpf": cpf})
    print('Cliente cadastrado com sucesso!')


def verificar_cliente_cpf(clientes, cpf):
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            return cliente
    return None
    
def consultar_cliente(clientes):
    cpf = input('Informe o seu cpf: ')
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print(cliente)

def gerar_numero():
    return rd(1000000000, 99999999999)


#verificar se o cpf está cadastrado em alguma conta
def verificar_conta_cpf(contas, cpf):
    for conta in contas:
        if conta['cpf'] == cpf:
            return conta
    return None

#cria uma nova conta
def criar_conta(AGENCIA, contas, clientes, saldo, extrato):
    cpf = input('Informe o seu cpf: ')
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            numero_conta  = gerar_numero()
            
            contas.append({'agencia': AGENCIA, 'numero_conta': numero_conta, 'saldo': saldo,'extrato': extrato, 'cpf': cpf})
            print('Conta criada com sucesso!')
        else:
            print('cliente não cadastrado!!')

#imprime as informações de uma conta
def consultar_conta(contas):
    cpf = input('Informe o seu cpf: ')
    conta = verificar_conta_cpf(contas, cpf)
    if conta:
        print(conta)
      
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
            conta_encontrada = False
            conta = verificar_conta_cpf(contas, cpf)
            if conta:
                conta_encontrada = True
                valor = float(input('Informe o valor que deseja depositar: '))
                conta['saldo'], conta['extrato'] = depositar(valor, conta['saldo'], conta['extrato'])
                    
                print('Deposito relizado com sucesso!\n')
            if not conta_encontrada:
                print('A operação falhou! Crie uma conta primeiro!\n')    
  
            print('\n---------------------------------------------\n')
        elif op == 2:
            print('\n---------------------------------------------\n')
            cpf = input('Informe o seu cpf: ')
            conta_encontrada = False
            
            conta = verificar_conta_cpf(contas, cpf)
            if conta:
                conta_encontrada = True
                conta['saldo'], conta['extrato'], numero_saques = sacar(conta['saldo'], conta['extrato'], numero_saques, LIMITE_SAQUES, limite)
                print('Saque realizado com sucesso!') 

            if not conta_encontrada:
                print('A operação falhou! Crie uma conta primeiro!\n')     
            print('\n---------------------------------------------\n')
        elif op == 3:
    
            imprimir_extrato(contas)
            
        elif op == 4:
            cadastrar_cliente(clientes)
            
            print(clientes)
            
        elif op == 5:
            criar_conta(AGENCIA, contas, clientes, saldo, extrato)
            
            print(contas)
        elif op == 6:
            consultar_conta(contas)
        elif op == 7:
            pass
        elif op == 8:
            print('Programa encerrado...\n ')
            break
        else:
            print('Opção inválida!!\n')

main()
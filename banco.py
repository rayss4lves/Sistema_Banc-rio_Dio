import conta as fco

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f'Deposito de: {valor:.2f}\n')
        print('Deposito relizado com sucesso!\n')
               
    else:
        print('Operação falhou, tente novamente!!\n')
    return saldo, extrato


#função para sacar o valor de uma determinada conta
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
            print('Saque realizado com sucesso!')
    else:
        print('Operação inválida! O numero de saques permitidos foi excedido!\n ')

    return saldo, extrato, numero_saques
 
 
def imprimir_extrato(contas):
    num_conta = int(input('Informe o numero da conta: '))
            
    conta = fco.verifica_numero_conta(contas, num_conta)
    if conta:
        print('\n-------------------EXTRATO-------------------\n')
        print(conta['extrato'])
        print(conta['saldo'])
        
        print('\n---------------------------------------------\n')
    else:
        print('Conta não encontrada!!')
 
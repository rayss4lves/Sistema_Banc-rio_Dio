def menu():
    print('\n=============================================')
    print('Informe o que deseja fazer:')
    print('1 - Depositar\n2 - Sacar\n3 - Extrato\n4 - Sair')
    print('=============================================\n')
    return int(input('= '))
 
extrato = ''
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
saldo = 0
 
while True:   
    op = menu()
    
    if op == 1:
        print('\n---------------------------------------------\n')
        valor = float(input('Informe o valor que deseja depositar: '))
        if valor > 0:
            saldo += valor
            extrato += f'Deposito de: {valor:.2f}\n'
            
        else:
            print('Operação falhou, tente novamente!!\n')
        print('\n---------------------------------------------\n')
    elif op == 2:
        print('\n---------------------------------------------\n')
        
        saque_excedido = numero_saques >= LIMITE_SAQUES
        if saque_excedido == False:
            valor = float(input('Informe o valor que deseja sacar: '))
    
            saldo_excedido = valor > saldo
            limite_excedido = valor > limite
            
            if saldo_excedido: 
                print('Saldo insuficiente!\n ')
            elif limite_excedido:
                print('Excedeu o limite de saque!\n ')   
            else:
                saldo-=valor
                extrato+= f'Saque de {valor:.2f}\n'
                numero_saques+=1 
            print('\n---------------------------------------------\n')

        else:
            print('O numero de saques permitidos foi excedido!\n ')
    elif op == 3:
        print('\n-------------------EXTRATO-------------------\n')
        print(extrato)
        print(f'Saldo total: {saldo:.2f}')
        print('\n---------------------------------------------\n')
    elif op == 4:
        print('Programa encerrado...\n ')
        break
    else:
        print('Opção inválida!!\n')


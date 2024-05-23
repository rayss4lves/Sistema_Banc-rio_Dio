def menu():
    print('\n=============================================')
    print('=\tInforme o que deseja fazer:         =')
    print('= \t1 - Depositar                       =\n= \t2 - Sacar                           =\n= \t3 - Extrato                         =\n= \t4 - Sair                           =')
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

            if valor > 0:
                saldo += valor
                extrato+= f'Depósito de {valor:.2f}\n'
                print('Deposito relizado com sucesso!\n')
               
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
                
            print('\n---------------------------------------------\n')
        elif op == 3:
            print(extrato)
            print(saldo)
            
        elif op == 4:
            print('Programa encerrado...\n ')
            break
        else:
            print('Opção inválida!!\n')

main()

import conta as fco
import banco as fb
import clientes as fc


def menu():
    print('\n=============================================')
    print('=\tInforme o que deseja fazer:         =')
    print('= \t1 - Depositar                       =\n= \t2 - Sacar                           =\n= \t3 - Extrato                         =\n= \t4 - Cadastrar cliente               =\n= \t5 - Criar conta                     =\n= \t6 - consultar conta                 =\n= \t7 - consultar cliente               =\n= \t8 - Listar contas                   =\n= \t9 - listar clientes                 =\n= \t10 - Sair                           =')
    print('=============================================\n')
    return int(input('= '))

#cria uma nova conta
 
      
def main(): 
    clientes = []
    contas = []
    extrato = []
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3
    saldo = 0
    AGENCIA = '0001'
    
    
    while True:   
        op = menu()
        
        if op == 1:
            print('\n---------------------------------------------\n')

            conta_encontrada = False

            num_conta = int(input('Informe o numero da conta: '))
            
            conta = fco.verifica_numero_conta(contas, num_conta)
            
            if conta:
                conta_encontrada = True
                valor = float(input('Informe o valor que deseja depositar: '))
                conta['saldo'], conta['extrato'] = fb.depositar(valor, conta['saldo'], conta['extrato'])
                                                        
            if not conta_encontrada:
                print('A operação falhou! Crie uma conta primeiro!\n')     
  
            print('\n---------------------------------------------\n')
        elif op == 2:
            print('\n---------------------------------------------\n')
            conta_encontrada = False
            num_conta = int(input('Informe o numero da conta: '))
            
            conta = fc.verifica_numero_conta(contas, num_conta)
            
            if conta:
                conta_encontrada = True
                conta['saldo'], conta['extrato'], numero_saques = fb.sacar(conta['saldo'], conta['extrato'], numero_saques, LIMITE_SAQUES, limite)
                 

            if not conta_encontrada:
                print('A operação falhou! Crie uma conta primeiro!\n')     
            print('\n---------------------------------------------\n')
        elif op == 3:
    
            fb.imprimir_extrato(contas)
            
        elif op == 4:
            fc.cadastrar_cliente(clientes)
            
            print(clientes)
            
        elif op == 5:
            fco.criar_conta(AGENCIA, contas, clientes, saldo, extrato)
            
            print(contas)
        elif op == 6:
            fco.consultar_conta(contas)
        elif op == 7:
            fc.consultar_cliente(clientes)
        elif op == 8:
            fco.listar_contas(contas)
        elif op == 9:
            fc.listar_clientes(clientes)
            
        elif op == 10:
            print('Programa encerrado...\n ')
            break
        else:
            print('Opção inválida!!\n')

main()
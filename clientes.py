           
def cadastrar_cliente(clientes):
    cpf = input('Informe o seu cpf(somente numeros): ')
    
    cliente = verificar_cliente_cpf(clientes, cpf)
    if cliente:
        print('Cliente já cadastrado anteriormente!\n')
        return
        
    nome = input('Informe o seu nome: ')
    data_nascimento = input('Informe a sua data de nascimento(dd-mm-aaaa): ')
    endereco = input('Informe o seu endereço (logradouro, nro - bairro - cidade/ sigla estado): ')
    
    clientes.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print('Cliente cadastrado com sucesso!')


def verificar_cliente_cpf(clientes, cpf):
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            return cliente
    return None
 
    
def consultar_cliente(clientes):
    cpf = input('Informe o seu cpf(somente numeros): ')
    cliente = verificar_cliente_cpf(clientes, cpf)
    if cliente:
        print(cliente)
    else:
        print('Cliente não cadastrado!')


#função para listar todos os clientes cadastrados
def listar_clientes(clientes):
    for cliente in clientes:
        print(cliente)

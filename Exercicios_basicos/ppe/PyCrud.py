import DB

def consultar(consulta):
    return DB.comGet(consulta)

def inserir(consulta):
    DB.comSet(consulta)


def conectar(operacao, query):
    if operacao == 1:
        print(consultar(query))
    elif operacao == 2 or operacao == 3 or operacao == 4:
        inserir(query)

    # 'select * from regions'
    # "insert into regions (region_id,region_name) values (1,'Nordeste')"
    # "Update regions set REGION_NAME = 'NORDESTE' where REGION_ID=1"
    # "Delete from regions where REGION_ID=1"

    # 1- Select
    # 2- Insert
    # 3- Update\
    # 4- Delete

#conectar(2, "insert into regions (region_id,region_name) values (seqregionID.nextval,'Nordeste')")


print('Olá!\n'
      'Qual Operação deseja realizar?\n'
      '1 - Consultar uma Região \n'
      '2 - Cadastrar nova Região \n'
      '3 - Atualizar uma Região\n'
      '4 - Deletar uma região')

operacao = int(input('informe o Código da operação desejada: '))

if operacao == 1:
    region = input('informe o codigo ou nome da Região: ')
    if region.isnumeric():
        consult = f'Select * from regions where region_id = {region}'
    else:
        consult = f"select * from regions where REGION_NAME = '{region}'"
    conectar(operacao, consult)
elif operacao == 2:
    region = input('Informe o nome da nova Região: ')
    consult = f"insert into regions (region_id,region_name) values (seqregionID.nextval,'{region}')"
    conectar(operacao, consult)
elif operacao == 3:
    regionId = int(input('Informe o código da região: '))
    regionName = input(f'Informe o Novo nome para a Região de código = {regionId} : ')
    consult = f"Update regions set REGION_NAME = '{regionName}' where REGION_ID={regionId}"
    conectar(operacao, consult)
elif operacao == 4:
    regionId = int(input('Informe o código da região: '))
    consult = f"Delete from regions where REGION_ID={regionId}"
    conectar(operacao, consult)

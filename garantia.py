#Criar uma cópia da planilha de garantia
import os
import json

ARQUIVO_JSON = 'garantias.json'
#Função para carregar os dados do arquivo toda vez que inicializa o programa
def carregar_dados():
    """Carrega os dados do arquivo JSON ou retorna uma lista vazia."""
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, 'r') as file:
            return json.load(file)
    return []

garantias = carregar_dados()

#Função para salvar dados
def salvar_dados(dados):
    """Salva os dados no arquivo JSON."""
    with open(ARQUIVO_JSON, 'w') as file:
        json.dump(dados, file, indent=4)

#Lista aonde irá ficar as garantias:

#Adicionar novo dicionario na lista
#Função de adicionar nova garantia:
def novaGarantia():
    vendedor = input('Digite o vendedor: ')
    pedido = input('Digite o N° do pedido: ')
    codigo = input('Código da peça: ')
    descricao = input('Digite o nome do produto: ')
    quantidade = input('Digite a quantidade: ')
    motivo = input('Digite o motivo da garantia: ')
    garantias.append({
        'ID' : len(garantias),
        'Vendedor' : vendedor,
        'Pedido' : pedido,
        'Codigo' : codigo,
        'Descricao' : descricao,
        'Quantidade' : quantidade,
        'Motivo' : motivo,
        'Status' : 'Aguardando',
        'Voucher' : 'Não gerado',
    })
    print('Garantia nova registrada! ID:', len(garantias)-1)
    print(50 * '-')

#Função de listar todas as garantias
def listarGarantias():
    print()
    print('Listando todas as garantias')
    for garantia in garantias:
        print(50 * '-')
        for chave, valor in garantia.items():
            print(chave, ':' ,valor)    
    print(50 * '-')

#Função para atualizar dados da garantia
def atualizarGarantia():
    listarGarantias()
    while True:
        try:
            contador = 0
            id = input('Qual o ID da garantia que gostaria de alterar? ')
            id = int(id)
        except ValueError:
            print('Digite um ID válido!')
        print(50 * '-')

        try:
            for chave, valor in garantias[id].items():
                print(contador, ')', chave, ':' ,valor)
                contador += 1
            alterar = input('Digite qual desses você quer alterar (Exceto o ID): ')

            if alterar == '1':
                print('Vendedor atual:', garantias[id]['Vendedor'])
                update = input('Para qual vendedor deseja alterar? ')
                garantias[id]['Vendedor'] = update
                print('Vendedor alterado com sucesso!')
                print(50 * '-')
                print()
            if alterar == '2':
                print('Pedido atual:', garantias[id]['Pedido'])
                update = input('Para qual pedido deseja alterar? ')
                garantias[id]['Pedido'] = update
                print('Pedido alterado com sucesso!')
                print(50 * '-')
                print()
            if alterar == '3':
                print('Código atual:', garantias[id]['Codigo'])
                update = input('Para qual Código deseja alterar? ')
                garantias[id]['Codigo'] = update
                print('Código alterado com sucesso!')
                print(50 * '-')
                print()
            if alterar == '4':
                print('Descrição atual:', garantias[id]['Descricao'])
                update = input('Para qual descrição deseja alterar? ')
                garantias[id]['Descricao'] = update
                print('Descrição alterado com sucesso!')
                print(50 * '-')
                print()
            if alterar == '5':
                print('Quantidade atual:', garantias[id]['Quantidade'])
                update = input('Para qual quantidade deseja alterar? ')
                garantias[id]['Quantidade'] = update
                print('Quantidade alterado com sucesso!')
                print(50 * '-')
                print()
            if alterar == '6':
                print('Motivo atual:', garantias[id]['Motivo'])
                update = input('Para qual motivo deseja alterar? ')
                garantias[id]['Motivo'] = update
                print('Motivo alterado com sucesso!')
                print(50 * '-')
                print()
            if alterar == '7':
                print('Status atual:', garantias[id]['Status'])
                update = input('Para qual status deseja alterar? ')
                garantias[id]['Status'] = update
                print('Status alterado com sucesso!')
                print(50 * '-')
                print()        
            if alterar == '8':
                print('Status do voucher atual:', garantias[id]['Voucher'])
                update = input('Para qual status deseja alterar? ')
                garantias[id]['Voucher'] = update
                print('Status do voucher alterado com sucesso!')
                print(50 * '-')
                print()
        except:
            print('Erro!')
            print('IDs válidos:')
            contagem = len(garantias) - 1
            print(contagem)
            for id in garantias:
                contagem -= 1
                if contagem != -1:
                    print(contagem)
                continue
            print(50 * '-')
        break

while True:
    print("1) Registrar nova garantia")
    print("2) Ver todas as garantias")
    print("3) Atualizar garantia")
    print("4) Sair")
    acao = input("O que você precisa? ")
    print(50 * '-')
    print()
    if acao == '1':
        novaGarantia()
        salvar_dados(garantias)
    elif acao == '2':
        listarGarantias()
    elif acao == '3':
        atualizarGarantia()
        salvar_dados(garantias)
    elif acao == '4':
        print('Finalizando o programa')
        break


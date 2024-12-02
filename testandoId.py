garantias = [
    {
        'ID' : '0',
        'nome' : 'Guilherme',
    },

    {
        'ID' : '1',
        'nome' : 'Lucas',
    }
]


def atualizarGarantia():
    listarGarantias()
    while True:
        try:
            contador = 0
            Label(nova)
            id = input('Qual o ID da garantia que gostaria de alterar? ')
            id = int(id)
        except ValueError:
            print('Digite um ID válido!')


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
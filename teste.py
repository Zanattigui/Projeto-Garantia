#Criar uma cópia da planilha de garantia
import os
import json
from tkinter import *

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


#Função de adicionar nova garantia:
def novaGarantia():
    nova = Tk()
    nova.title('Registrar nova garantia')
    #Label, estou fazendo a caixa aonde mostra o texto "Vendedor:":
    Label(nova, text='Vendedor:').grid(column=0, row=0)
    #Gerando um "input" para o usuario:
    entrada_vendedor = Entry(nova)
    #Ajeitando a coluna e a linha:
    entrada_vendedor.grid(column=1, row=0)

    Label(nova, text='Pedido:').grid(column=0, row=1)
    entrada_pedido = Entry(nova)
    entrada_pedido.grid(column=1, row=1)
    Label(nova, text='Código da peça:').grid(column=0, row=2)
    entrada_codigo = Entry(nova)
    entrada_codigo.grid(column=1, row=2)
    Label(nova, text='Descrição:').grid(column=0, row=3)
    entrada_descricao = Entry(nova)
    entrada_descricao.grid(column=1, row=3)
    Label(nova, text='Quantidade:').grid(column=0, row=4)
    entrada_quantidade = Entry(nova)
    entrada_quantidade.grid(column=1, row=4)
    Label(nova, text='Motivo:').grid(column=0, row=5)
    entrada_motivo = Entry(nova)
    entrada_motivo.grid(column=1, row=5)

    def salvar():
        garantias.append({
            'ID' : len(garantias),
            'Vendedor' : entrada_vendedor.get(), #Usando o metodo .get para pegar o que esta dentro do entrada_vendedor
            'Pedido' : entrada_pedido.get(),
            'Codigo' : entrada_codigo.get(),
            'Descricao' : entrada_descricao.get(),
            'Quantidade' : entrada_quantidade.get(),
            'Motivo' : entrada_motivo.get(),
            'Status' : 'Aguardando',
            'Voucher' : 'Não gerado',
        })
        salvar_dados(garantias)
        nova.destroy()

    Button(nova, text='SALVAR', command=salvar).grid(columnspan=2, row=6)

#Função de listar todas as garantias
def listarGarantias():

    todasAsGarantias = Tk()
    todasAsGarantias.title('Todas as garantias')

    #Titulos
    tituloId = Label(todasAsGarantias, text='ID')
    tituloId.grid(column=0, row= 0)
    tituloVendedor = Label(todasAsGarantias, text='Vendedor')
    tituloVendedor.grid(column=1, row= 0)
    tituloPedido = Label(todasAsGarantias, text='Pedido')
    tituloPedido.grid(column=2, row= 0)
    tituloCodigo = Label(todasAsGarantias, text='Código')
    tituloCodigo.grid(column=3, row= 0)
    tituloDescricao = Label(todasAsGarantias, text='Descrição')
    tituloDescricao.grid(column=4, row= 0)
    tituloQuantidade = Label(todasAsGarantias, text='Quantidade')
    tituloQuantidade.grid(column=5, row= 0)
    tituloMotivo = Label(todasAsGarantias, text='Motivo')
    tituloMotivo.grid(column=6, row= 0)
    tituloStatus = Label(todasAsGarantias, text='Status')
    tituloStatus.grid(column=7, row= 0)
    tituloVoucher = Label(todasAsGarantias, text='Voucher')
    tituloVoucher.grid(column=8, row= 0)

    #Listando os valores das garantias
    linha = 1
    for garantia in garantias:
        id_label = Label(todasAsGarantias, text=garantia['ID'])
        id_label.grid(column=0, row=linha)
        vendedor_label = Label(todasAsGarantias, text=garantia['Vendedor'])
        vendedor_label.grid(column=1, row=linha)
        pedido_label = Label(todasAsGarantias, text=garantia['Pedido'])
        pedido_label.grid(column=2, row=linha)
        codigo_label = Label(todasAsGarantias, text=garantia['Codigo'])
        codigo_label.grid(column=3, row=linha)
        descricao_label = Label(todasAsGarantias, text=garantia['Descricao'])
        descricao_label.grid(column=4, row=linha)
        quantidade_label = Label(todasAsGarantias, text=garantia['Quantidade'])
        quantidade_label.grid(column=5, row=linha)
        motivo_label = Label(todasAsGarantias, text=garantia['Motivo'])
        motivo_label.grid(column=6, row=linha)
        status_label = Label(todasAsGarantias, text=garantia['Status'])
        status_label.grid(column=7, row=linha)
        voucher_label = Label(todasAsGarantias, text=garantia['Voucher'])
        voucher_label.grid(column=8, row=linha)
        linha += 1

#Função para atualizar dados da garantia
def atualizarGarantia():
    atualizar = Tk()
    atualizar.title('Atualizar garantia')

    listarGarantias()
    while True:
        try:
            contador = 0
            Label(atualizar, text='Qual o ID da garantia que gostaria de alterar?').grid(column=0, row=0)
            entrada_id = Entry(atualizar)
            entrada_id.grid(column=0, row=1)
            entrada_id = int(id)
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

principal = Tk()
#Titulo da janela:
principal.title('Garantias')
#Criando a janela para listar todas as garantias:

textoTitulo = Label(principal, text='Garantias Neotech')
textoTitulo.grid(column=1, row=0)

botaoTodasAsGarantias = Button(principal, text='Todas as garantias', command=listarGarantias)
botaoTodasAsGarantias.grid(column=0, row=1)

botaoNovaGarantia = Button(principal, text='Registrar nova garantia', command=novaGarantia)
botaoNovaGarantia.grid(column=2, row=1)

botaoAtualizarGarantia = Button(principal, text='Atualizar garantia', command=atualizarGarantia)
botaoAtualizarGarantia.grid(column=3, row=1)


principal.mainloop()

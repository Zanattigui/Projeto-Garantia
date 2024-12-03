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
    
    #Titulo ID e Pedido:
    tituloId = Label(atualizar, text='ID')
    tituloId.grid(column=0, row= 0)
    tituloPedido = Label(atualizar, text='Pedido')
    tituloPedido.grid(column=1, row=0)
    
    #listando Id's e pedido para ver qual o ususario vai querer alterar:
    linha = 1
    for garantia in garantias:
        id_label = Label(atualizar, text=garantia['ID'])
        id_label.grid(column=0, row=linha)
        pedido_label = Label(atualizar, text=garantia['Pedido'])
        pedido_label.grid(column=1, row=linha)
        linha += 1

    #Exibindo a caixa de pergunta e a caixa de resposta do usuario:
    try:
        Label(atualizar, text='Qual o ID da garantia que gostaria de alterar?').grid(column=0, row=linha)
        entrada_id = Entry(atualizar)
        entrada_id.grid(column=1, row=linha)
    except ValueError:
        Label(atualizar, text='Digite um ID válido.')

    def enter_id():
        atualizarDados = Tk()
        atualizarDados.title('Atualizar dados')

        #Transformando em inteiro para poder puxar por indice no dicionario:
        int_id = entrada_id.get()
        int_id = int(int_id)

        #Titulos
        tituloId = Label(atualizarDados, text='ID:')
        tituloId.grid(column=1, row= 0)
        tituloVendedor = Label(atualizarDados, text='1) Vendedor:')
        tituloVendedor.grid(column=1, row= 1)
        tituloPedido = Label(atualizarDados, text='2) Pedido:')
        tituloPedido.grid(column=1, row= 2)
        tituloCodigo = Label(atualizarDados, text='3) Código:')
        tituloCodigo.grid(column=1, row= 3)
        tituloDescricao = Label(atualizarDados, text='4) Descrição:')
        tituloDescricao.grid(column=1, row= 4)
        tituloQuantidade = Label(atualizarDados, text='5) Quantidade:')
        tituloQuantidade.grid(column=1, row= 5)
        tituloMotivo = Label(atualizarDados, text='6) Motivo:')
        tituloMotivo.grid(column=1, row= 6)
        tituloStatus = Label(atualizarDados, text='7) Status:')
        tituloStatus.grid(column=1, row= 7)
        tituloVoucher = Label(atualizarDados, text='8) Voucher:')
        tituloVoucher.grid(column=1, row= 8)

        #Valores:
        id_label = Label(atualizarDados, text=garantias[int_id]['ID'])
        id_label.grid(column=2, row=0)
        vendedor_label = Label(atualizarDados, text=garantias[int_id]['Vendedor'])
        vendedor_label.grid(column=2, row=1)
        pedido_label = Label(atualizarDados, text=garantias[int_id]['Pedido'])
        pedido_label.grid(column=2, row=2)
        codigo_label = Label(atualizarDados, text=garantias[int_id]['Codigo'])
        codigo_label.grid(column=2, row=3)
        descricao_label = Label(atualizarDados, text=garantias[int_id]['Descricao'])
        descricao_label.grid(column=2, row=4)
        quantidade_label = Label(atualizarDados, text=garantias[int_id]['Quantidade'])
        quantidade_label.grid(column=2, row=5)
        motivo_label = Label(atualizarDados, text=garantias[int_id]['Motivo'])
        motivo_label.grid(column=2, row=6)
        status_label = Label(atualizarDados, text=garantias[int_id]['Status'])
        status_label.grid(column=2, row=7)
        voucher_label = Label(atualizarDados, text=garantias[int_id]['Voucher'])
        voucher_label.grid(column=2, row=8)
        #Fecha a aba "Atualizar":
        atualizar.destroy()
        
        
        def enter_item():
            alterando_item = Tk()
            alterando_item.title('Alterando item')
            #Se alterar item for igual a 1 entao tem que aparecer uma caixinha com o atual vendedor
            if alterar_item == 1:
                Label(alterando_item, text='Vendedor atual:').grid(column=0, row=0)
                Label(alterando_item, text=garantias[int_id]['Vendedor']).grid(column=1, row=0)
                Label(alterando_item, text='Para qual vendedor deseja alterar?').grid(column=0, row=1)
                update = Entry(alterando_item)
                update.grid(colum=1, row=1)               
                garantias[int_id]['Vendedor'] = update
                Label(alterando_item, text='Vendedor alterado para:').grid(column=0, row=2)
                Label(alterando_item, text=garantias[int_id]['Vendedor']).grid(column=1, row=2)

        alterar_item = Entry(atualizarDados)
        alterar_item.grid(column=2, row=9)

        Button(atualizarDados, text='Enter', command=enter_item).grid(column=3, row=9)

        Label(atualizarDados, text='Qual item gostaria de alterar?').grid(column=0, columnspan=2, row=9)




    linha += 1
    Button(atualizar, text='Enter', command=enter_id).grid(columnspan=4, row=linha)
    
    


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

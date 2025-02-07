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
    row = 0
    column = 0
    #Titulos
    keyList = list(garantias[0].keys())
    for key in keyList:
        tituloId = Label(todasAsGarantias, text=key)
        tituloId.grid(column=column, row= row)
        column += 1
    #Listando os valores das garantias
    row = 1
    column = 0
    for key in keyList:
        for garantia in garantias:
            id_label = Label(todasAsGarantias, text=garantia[key])
            id_label.grid(column=column, row=row)
            row += 1 
        column += 1
        row = 1
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

    #Exibindo a caixa de pergunta para ver qual o id da garantia o usuario quer mexer:
    try:
        Label(atualizar, text='Qual o ID da garantia que gostaria de alterar?').grid(column=0, row=linha)
        #Caixa de entrada de texto para informar o ID
        entrada_id = Entry(atualizar)
        entrada_id.grid(column=1, row=linha)
    #Caso digite um ID invalido:
    except ValueError:
        Label(atualizar, text='Digite um ID válido.')

    #Função para abrir nova janela e mudar algum item da garantia
    def enter_id():
        atualizarDados = Tk()
        atualizarDados.title('Atualizar dados')

        #Função para alterar vendedor:
        def mudando_vendedor():
            #Caixa perguntando qual vendedor vai alterar:
            Label(atualizarDados, text='Para qual vendedor deseja alterar?').grid(column=0, row=10)
            #Variavel criada para guardar o dado que o usuario inserir
            alterar_item = Entry(atualizarDados)
            alterar_item.grid(column=1, row=10)

            #Função para salvar mudança de vendedor:
            def salvar_vendedor():
                #Variavel criada para armazenar a entrada em alterar_item, utilizando o metodo .get() para pegar o valor de alterar_item
                update = alterar_item.get()    
                #Alterando vendedor com 'update'
                garantias[int_id]['Vendedor'] = update
                Label(atualizarDados, text='Vendedor alterado para:').grid(column=0, row=11)
                Label(atualizarDados, text=garantias[int_id]['Vendedor']).grid(column=1,row=11)

            #Botao para chamar a função "salvar_vendedor"
            Button(atualizarDados, text= 'salvar', command=salvar_vendedor).grid(column=2, row=10)
        #Função para alterar pedido
        def mudando_pedido():

            Label(atualizarDados, text='Para qual pedido deseja alterar?').grid(column=0, row=10)

            alterar_item = Entry(atualizarDados)
            alterar_item.grid(column=1, row=10)

            def salvar_pedido():

                update = alterar_item.get()    
                garantias[int_id]['Pedido'] = update

                Label(atualizarDados, text='Pedido alterado para:').grid(column=0, row=11)
                Label(atualizarDados, text=garantias[int_id]['Pedido']).grid(column=1,row=11)

            Button(atualizarDados, text= 'salvar', command=salvar_pedido).grid(column=2, row=10)
        #Função para alterar código
        def mudando_codigo():

            Label(atualizarDados, text='Para qual código deseja alterar?').grid(column=0, row=10)

            alterar_item = Entry(atualizarDados)
            alterar_item.grid(column=1, row=10)

            def salvar_codigo():

                update = alterar_item.get()    
                garantias[int_id]['Codigo'] = update

                Label(atualizarDados, text='Código alterado para:').grid(column=0, row=11)
                Label(atualizarDados, text=garantias[int_id]['Codigo']).grid(column=1,row=11)

            Button(atualizarDados, text= 'salvar', command=salvar_codigo).grid(column=2, row=10)       
        #Função para alterar descrição   
        def mudando_descricao():

            Label(atualizarDados, text='Para qual descrição deseja alterar?').grid(column=0, row=10)

            alterar_item = Entry(atualizarDados)
            alterar_item.grid(column=1, row=10)

            def salvar_descricao():

                update = alterar_item.get()    
                garantias[int_id]['Descricao'] = update

                Label(atualizarDados, text='Descrição alterado para:').grid(column=0, row=11)
                Label(atualizarDados, text=garantias[int_id]['Descricao']).grid(column=1,row=11)

            Button(atualizarDados, text= 'Salvar', command=salvar_descricao).grid(column=2, row=10)             
        #Função para alterar quantidade        
        def mudando_quantidade():

            Label(atualizarDados, text='Para qual quantidade deseja alterar?').grid(column=0, row=10)

            alterar_item = Entry(atualizarDados)
            alterar_item.grid(column=1, row=10)

            def salvar_quantidade():

                update = alterar_item.get()    
                garantias[int_id]['Quantidade'] = update

                Label(atualizarDados, text='Quantidade alterado para:').grid(column=0, row=11)
                Label(atualizarDados, text=garantias[int_id]['Quantidade']).grid(column=1,row=11)

            Button(atualizarDados, text= 'Salvar', command=salvar_quantidade).grid(column=2, row=10)                    
        #Função para alterar motivo        
        def mudando_motivo():

            Label(atualizarDados, text='Para qual motivo deseja alterar?').grid(column=0, row=10)

            alterar_item = Entry(atualizarDados)
            alterar_item.grid(column=1, row=10)

            def salvar_motivo():

                update = alterar_item.get()    
                garantias[int_id]['Motivo'] = update

                Label(atualizarDados, text='Motivo alterado para:').grid(column=0, row=11)
                Label(atualizarDados, text=garantias[int_id]['Motivo']).grid(column=1,row=11)

            Button(atualizarDados, text= 'Salvar', command=salvar_motivo).grid(column=2, row=10)            
        #Função para alterar status       
        def mudando_status():

            Label(atualizarDados, text='Para qual status deseja alterar?').grid(column=0, row=10)

            alterar_item = Entry(atualizarDados)
            alterar_item.grid(column=1, row=10)

            def salvar_status():

                update = alterar_item.get()    
                garantias[int_id]['Status'] = update

                Label(atualizarDados, text='Status alterado para:').grid(column=0, row=11)
                Label(atualizarDados, text=garantias[int_id]['Status']).grid(column=1,row=11)

            Button(atualizarDados, text= 'Salvar', command=salvar_status).grid(column=2, row=10)            
        #Função para alterar voucher        
        def mudando_voucher():

            Label(atualizarDados, text='Para qual voucher deseja alterar?').grid(column=0, row=10)

            alterar_item = Entry(atualizarDados)
            alterar_item.grid(column=1, row=10)

            def salvar_voucher():

                update = alterar_item.get()    
                garantias[int_id]['Voucher'] = update

                Label(atualizarDados, text='Voucher alterado para:').grid(column=0, row=11)
                Label(atualizarDados, text=garantias[int_id]['Voucher']).grid(column=1,row=11)

            Button(atualizarDados, text= 'Salvar', command=salvar_voucher).grid(column=2, row=10)    
        
       
        #Transformando em inteiro para poder puxar por indice no dicionario:
        try:
            int_id = int(entrada_id.get())
        except ValueError:
            Label(atualizar, text="Erro: Digite um número válido para o ID.").grid(column=0, row=linha+1)
            return

        Label(atualizarDados, text='Clique em qual gostaria de alterar:').grid(column=0, columnspan=1, row=0)

        #Titulos
        tituloId = Label(atualizarDados, text='ID:')
        tituloId.grid(column=0, row= 1)
        tituloVendedor = Button(atualizarDados, text='1) Vendedor:', command=mudando_vendedor)
        tituloVendedor.grid(column=0, row= 2)
        tituloPedido = Button(atualizarDados, text='2) Pedido:', command=mudando_pedido)
        tituloPedido.grid(column=0, row= 3)
        tituloCodigo = Button(atualizarDados, text='3) Código:', command=mudando_codigo)
        tituloCodigo.grid(column=0, row= 4)
        tituloDescricao = Button(atualizarDados, text='4) Descrição:', command=mudando_descricao)
        tituloDescricao.grid(column=0, row= 5)
        tituloQuantidade = Button(atualizarDados, text='5) Quantidade:', command=mudando_quantidade)
        tituloQuantidade.grid(column=0, row=6)
        tituloMotivo = Button(atualizarDados, text='6) Motivo:', command=mudando_motivo)
        tituloMotivo.grid(column=0, row= 7)
        tituloStatus = Button(atualizarDados, text='7) Status:', command=mudando_status)
        tituloStatus.grid(column=0, row= 8)
        tituloVoucher = Button(atualizarDados, text='8) Voucher:', command=mudando_voucher)
        tituloVoucher.grid(column=0, row= 9)

        #Valores:
        id_label = Label(atualizarDados, text=garantias[int_id]['ID'])
        id_label.grid(column=1, row=1)
        vendedor_label = Label(atualizarDados, text=garantias[int_id]['Vendedor'])
        vendedor_label.grid(column=1, row=2)
        pedido_label = Label(atualizarDados, text=garantias[int_id]['Pedido'])
        pedido_label.grid(column=1, row=3)
        codigo_label = Label(atualizarDados, text=garantias[int_id]['Codigo'])
        codigo_label.grid(column=1, row=4)
        descricao_label = Label(atualizarDados, text=garantias[int_id]['Descricao'])
        descricao_label.grid(column=1, row=5)
        quantidade_label = Label(atualizarDados, text=garantias[int_id]['Quantidade'])
        quantidade_label.grid(column=1, row=6)
        motivo_label = Label(atualizarDados, text=garantias[int_id]['Motivo'])
        motivo_label.grid(column=1, row=7)
        status_label = Label(atualizarDados, text=garantias[int_id]['Status'])
        status_label.grid(column=1, row=8)
        voucher_label = Label(atualizarDados, text=garantias[int_id]['Voucher'])
        voucher_label.grid(column=1, row=9)
        #Fecha a aba "Atualizar":
        atualizar.destroy()


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

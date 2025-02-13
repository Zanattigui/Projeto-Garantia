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
    row = 0
    column = 0
    #Titulos utilizando uma limitação para puxar somente até o indice 6 ([:6])
    keyList = list(garantias[0].keys())
    for key in keyList[:6]:
        tituloId = Label(nova, text=key)
        tituloId.grid(column=column, row= row)
        row += 1

    #Gerando um "input" para o usuario:
    entrada_vendedor = Entry(nova)
    #Ajeitando a coluna e a linha:
    entrada_vendedor.grid(column=1, row=0)

    entrada_pedido = Entry(nova)
    entrada_pedido.grid(column=1, row=1)
    
    entrada_codigo = Entry(nova)
    entrada_codigo.grid(column=1, row=2)
    
    entrada_descricao = Entry(nova)
    entrada_descricao.grid(column=1, row=3)
   
    entrada_quantidade = Entry(nova)
    entrada_quantidade.grid(column=1, row=4)
    
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
    Label(atualizar, text='ID').grid(column=0, row= 0)
    Label(atualizar, text='Pedido').grid(column=1, row=0)
    
    #listando Id's e pedidos para ver qual o usuario vai querer alterar:
    row = 1
    for garantia in garantias:
        id_label = Label(atualizar, text=garantia['ID'])
        id_label.grid(column=0, row=row)
        pedido_label = Label(atualizar, text=garantia['Pedido'])
        pedido_label.grid(column=1, row=row)
        row += 1

    #Exibindo a caixa de pergunta para ver qual o id da garantia o usuario quer mexer:
    try:
        Label(atualizar, text='Qual o ID da garantia que gostaria de alterar?').grid(column=0, row=row)
        #Caixa de entrada de texto para informar o ID
        entrada_id = Entry(atualizar)
        entrada_id.grid(column=1, row=row)
    #Caso digite um ID invalido:
    except ValueError:
        Label(atualizar, text='Digite um ID válido.')

    #Função para abrir nova janela e mudar algum item da garantia
    def enter_id():
        atualizarDados = Tk()
        atualizarDados.title('Atualizar dados')

        #Transformando em inteiro para poder puxar por indice no dicionario:
        try:
            int_id = int(entrada_id.get())
        except ValueError:
            Label(atualizar, text="Erro: Digite um número válido para o ID.").grid(column=0, row=row+1)
            return

        #Titulos
        row = 1
        cont = 0
        keyList = list(garantias[0].keys())
        for key in keyList:
            tituloId = Label(atualizarDados, text=f'{cont}) {key}')
            tituloId.grid(column=0, row= row)
            row += 1
            cont +=1
        row = 1
        
        #Valores:
        for key in keyList:
            id_label = Label(atualizarDados, text=garantias[int_id][key])
            id_label.grid(column=1, row=row)
            row += 1

        Label(atualizarDados, text='Digite o numero do item que deseja alterar:').grid(column=0, row=9)
        atualizationId = Entry(atualizarDados)
        atualizationId.grid(column=1, row=9)
        
        def atualizationValue ():

            id_key = int(atualizationId.get())
            id_key = keyList[id_key]
            #Função para alterar pedido
            Label(atualizarDados, text=f'Para qual {id_key} deseja alterar?').grid(column=0, row=11)

            alterar_item = Entry(atualizarDados)
            alterar_item.grid(column=1, row=11)
            
            #Função de salvar a atualização
            def atualizationSave():
                update = alterar_item.get()    
                garantias[int_id][id_key] = update

                Label(atualizarDados, text=f'{id_key} alterado para:').grid(column=0, row=12)
                Label(atualizarDados, text=garantias[int_id][id_key]).grid(column=1,row=12)
                Label(atualizarDados, text= 'Essa janela irá fechar automaticamente após 5 segundos!').grid(columnspan=3 , row=13)
                atualizarDados.after(5000, atualizarDados.destroy)
            #Botao de salvar apos alterado
            Button(atualizarDados, text= 'Salvar', command=atualizationSave).grid(column=2, row=11)
        
        Button(atualizarDados, text='Enter', command=atualizationValue).grid(columnspan=2, row=10)


        #Fecha a aba "Atualizar":
        atualizar.destroy()


    row += 1
    Button(atualizar, text='Enter', command=enter_id).grid(columnspan=4, row=row)
    
    


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

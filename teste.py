dictonary = [
    {
        "ID": 0,
        "Vendedor": "Cadmiel",
        "Pedido": "15643",
        "Codigo": "NEOUS110234",
        "Descricao": "Injetor",
        "Quantidade": "1",
        "Motivo": "Falhando",
        "Status": "Aguardando",
        "Voucher": "N\u00e3o gerado"
    },
    {
        "ID": 1,
        "Vendedor": "Lucas",
        "Pedido": "14532",
        "Codigo": "NEO461409",
        "Descricao": "Jogo de reparo",
        "Quantidade": "1",
        "Motivo": "Faltando pe\u00e7as",
        "Status": "Aguardando",
        "Voucher": "N\u00e3o gerado"
    }
]
keyList = list(dictonary[0].keys())
atualizationId = input()
atualizationId = int(atualizationId)
atualizationId = keyList[atualizationId]

def funcao():
    return print(atualizationId)

funcao()
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


# for item in dictonary:
       # print(dictonary[item])

valueList = list(dictonary[0].values())
for value in valueList:
    print(value)
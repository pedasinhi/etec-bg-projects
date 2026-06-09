ValorProduto = float(input("Digite um valor de um produto: "))
QuantidadeProduto = int(input("Digite a quantidade: "))

def CheckProduto(valor, quantidade):
    return(valor * quantidade)

print(f"O valor total de sua compra é de {CheckProduto(ValorProduto, QuantidadeProduto)}")
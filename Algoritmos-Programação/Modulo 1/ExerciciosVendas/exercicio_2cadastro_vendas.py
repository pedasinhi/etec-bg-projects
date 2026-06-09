def cadastrar_produtos():
    produtos = []
    quantidade = int(input("Quantos produtos serao cadastrados? "))

    for i in range(quantidade):
        print(f"\n--- Cadastro do Produto {i + 1} ---")
        nome = input("Nome do produto: ")
        preco = float(input("Preco: R$ ").replace(",", "."))
        estoque = int(input("Quantidade em estoque: "))

        produto = {
            "nome": nome,
            "preco": preco,
            "estoque": estoque
        }
        produtos.append(produto)

    return produtos


def buscar_produto(produtos, nome_buscado):
    for produto in produtos:
        if produto["nome"].lower() == nome_buscado.lower():
            return produto
    return None


def aplicar_desconto(total):
    if total >= 1000:
        percentual = 15
        desconto = total * 0.15
    elif total >= 500 and total < 1000:
        percentual = 10
        desconto = total * 0.10
    elif total >= 200 and total < 500:
        percentual = 5
        desconto = total * 0.05
    else:
        percentual = 0
        desconto = 0.0

    return percentual, desconto


def exibir_resumo(nome_cliente, itens_comprados, total, percentual, desconto, total_final):
    print("\n" + "=" * 45)
    print("            RESUMO DA COMPRA")
    print("=" * 45)
    print(f"Cliente: {nome_cliente}")
    print("\nProdutos comprados:")

    for item in itens_comprados:
        print(f"  - {item['nome']} | {item['qtd']}x R$ {item['preco']:.2f} = R$ {item['subtotal']:.2f}")

    print(f"\nTotal da compra:  R$ {total:.2f}")
    print(f"Desconto ({percentual}%):   R$ {desconto:.2f}")
    print(f"Total final:      R$ {total_final:.2f}")
    print("=" * 45)


print("=" * 45)
print("   SISTEMA DE CADASTRO E VENDAS")
print("=" * 45)

produtos = cadastrar_produtos()
print(f"\n{len(produtos)} produto(s) cadastrado(s) com sucesso!")

nome_cliente = input("\nDigite o nome do cliente: ")
itens_comprados = []
total = 0.0

continuar_comprando = "S"

while continuar_comprando != "N":
    nome_desejado = input("\nDigite o nome do produto desejado: ")

    produto_encontrado = buscar_produto(produtos, nome_desejado)

    if produto_encontrado is None:
        print("Produto nao encontrado. Tente novamente.")
    else:
        quantidade_desejada = int(input(f"Quantidade desejada (estoque: {produto_encontrado['estoque']}): "))

        if quantidade_desejada > produto_encontrado["estoque"]:
            print("Quantidade maior que o estoque disponivel!")
        else:
            subtotal = produto_encontrado["preco"] * quantidade_desejada
            total += subtotal

            itens_comprados.append({
                "nome": produto_encontrado["nome"],
                "qtd": quantidade_desejada,
                "preco": produto_encontrado["preco"],
                "subtotal": subtotal
            })

            produto_encontrado["estoque"] -= quantidade_desejada
            print(f"Subtotal: R$ {subtotal:.2f}")

    continuar_comprando = input("\nDeseja continuar comprando? (S/N): ").upper()

percentual, desconto = aplicar_desconto(total)
total_final = total - desconto

exibir_resumo(nome_cliente, itens_comprados, total, percentual, desconto, total_final)

print("\nObrigado pela compra! Ate logo!")

def calcular_subtotal(preco, quantidade):
    # Multiplica preço pela quantidade comprada
    return preco * quantidade

def aplicar_desconto(total):
    # Aplica desconto baseado no valor total da compra
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
        desconto = 0

    return percentual, desconto

def calcular_media(historico_vendas):
    # Calcula média das vendas
    if len(historico_vendas) == 0:
        return 0
    total_faturado = 0
    for venda in historico_vendas:
        total_faturado += venda["total_final"]
    return total_faturado / len(historico_vendas)

def encontrar_maior_compra(historico_vendas):
    # Encontra a maior venda do histórico
    maior = historico_vendas[0]
    for venda in historico_vendas:
        if venda["total_final"] > maior["total_final"]:
            maior = venda
    return maior


def buscar_produto(produtos, nome_buscado):
    # Procura um produto pelo nome (sem diferenciar maiúsculas/minúsculas)
    for produto in produtos:
        if produto["nome"].lower() == nome_buscado.lower():
            return produto
    return None


def exibir_resumo_venda(venda):
    # Mostra detalhes de uma venda específica
    print(f"\n  Cliente: {venda['cliente']}")
    print(f"  Itens comprados:")
    for item in venda["itens"]:
        print(f"    - {item['nome']} | {item['qtd']}x R$ {item['preco']:.2f} = R$ {item['subtotal']:.2f}")
    print(f"  Total bruto:  R$ {venda['total_bruto']:.2f}")
    print(f"  Desconto ({venda['percentual']}%): R$ {venda['desconto']:.2f}")
    print(f"  Total final:  R$ {venda['total_final']:.2f}")

def exibir_relatorio(historico_vendas):
    # Gera relatório geral das vendas
    total_faturado = 0
    for venda in historico_vendas:
        total_faturado += venda["total_final"]

    media = calcular_media(historico_vendas)
    maior_venda = encontrar_maior_compra(historico_vendas)

    print("\n" + "=" * 50)
    print("         RELATÓRIO GERAL DA LOJA")
    print("=" * 50)
    print(f"Total de vendas realizadas: {len(historico_vendas)}")
    print(f"Valor total faturado:       R$ {total_faturado:.2f}")
    print(f"Cliente que mais comprou:   {maior_venda['cliente']} (R$ {maior_venda['total_final']:.2f})")
    print(f"Média de valor das vendas:  R$ {media:.2f}")
    print("=" * 50)

print("=" * 50)
print("    SISTEMA DE VENDAS COM RELATÓRIO")
print("=" * 50)

produtos = []  # Lista onde os produtos serão armazenados
qtd_produtos = int(input("\nQuantos produtos deseja cadastrar? "))

# Cadastro dos produtos
for i in range(qtd_produtos):
    
    print(f"\n--- Produto {i + 1} ---")
    nome_p = input("Nome: ")
    preco_p = float(input("Preço: R$ ").replace(",", "."))
    estoque_p = int(input("Estoque: "))

    produtos.append({
        "nome": nome_p,
        "preco": preco_p,
        "estoque": estoque_p
    })

print(f"\n{len(produtos)} produto(s) cadastrado(s) com sucesso!")

historico_vendas = []  # Guarda todas as vendas
nova_venda = "S"

# Loop principal de vendas
while nova_venda != "N":

    nome_cliente = input("\nNome do cliente: ")
    itens_comprados = []
    total_bruto = 0

    continuar_item = "S"

    # Loop para adicionar produtos na venda
    while continuar_item != "N":

        nome_desejado = input("\nDigite o nome do produto: ")
        produto = buscar_produto(produtos, nome_desejado)

        if produto is None:
            print("Produto não encontrado!")
        else:
            qtd_desejada = int(input(f"Quantidade (estoque: {produto['estoque']}): "))

            if qtd_desejada <= 0:
                print("Quantidade inválida.")
            elif qtd_desejada > produto["estoque"]:
                print("Estoque insuficiente!")
            else:
                subtotal = calcular_subtotal(produto["preco"], qtd_desejada)
                total_bruto += subtotal

                itens_comprados.append({
                    "nome": produto["nome"],
                    "qtd": qtd_desejada,
                    "preco": produto["preco"],
                    "subtotal": subtotal
                })

                produto["estoque"] -= qtd_desejada  # Atualiza estoque
                print(f"Subtotal: R$ {subtotal:.2f}")

        continuar_item = input("Continuar comprando itens? (S/N): ").upper()

    # Aplica desconto e calcula total final
    percentual, desconto = aplicar_desconto(total_bruto)
    total_final = total_bruto - desconto

    # Salva venda no histórico
    historico_vendas.append({
        "cliente": nome_cliente,
        "itens": itens_comprados,
        "total_bruto": total_bruto,
        "percentual": percentual,
        "desconto": desconto,
        "total_final": total_final
    })

    print(f"\nVenda registrada! Total final: R$ {total_final:.2f} (desconto de {percentual}%)")

    nova_venda = input("\nRealizar nova venda? (S/N): ").upper()

# Se não houver vendas
if len(historico_vendas) == 0:
    print("\nNenhuma venda realizada.")
else:
    print("\n" + "=" * 50)
    print("         RESUMO DE CADA VENDA")
    print("=" * 50)

    # Mostra cada venda
    for i, venda in enumerate(historico_vendas):
        print(f"\n  Venda #{i + 1}")
        print("  " + "-" * 40)
        exibir_resumo_venda(venda)

    # Mostra relatório final
    exibir_relatorio(historico_vendas)

print("\nSistema encerrado. Obrigado!")
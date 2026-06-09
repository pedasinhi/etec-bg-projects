continuar = "S"

while continuar != "N":

    nome_cliente = input("\nDigite o nome do cliente: ")
    quantidade_produtos = int(input("Quantos produtos serão comprados? "))

    total = 0.0

    for i in range(quantidade_produtos):
        print(f"\n--- Produto {i + 1} ---")
        nome_produto = input("Nome do produto: ")
        preco = float(input("Preço do produto: R$ ").replace(",", "."))
        quantidade = int(input("Quantidade: "))

        subtotal = preco * quantidade
        print(f"Subtotal: R$ {subtotal:.2f}")

        total += subtotal

    if total >= 500:
        percentual_desconto = 10
        desconto = total * 0.10
    elif total >= 200 and total < 500:
        percentual_desconto = 5
        desconto = total * 0.05
    else:
        percentual_desconto = 0
        desconto = 0.0

    total_final = total - desconto

    print("\n" + "=" * 40)
    print("          RESUMO DA COMPRA")
    print("=" * 40)
    print(f"Cliente:        {nome_cliente}")
    print(f"Total da compra: R$ {total:.2f}")
    print(f"Desconto ({percentual_desconto}%):  R$ {desconto:.2f}")
    print(f"Total final:    R$ {total_final:.2f}")
    print("=" * 40)

    continuar = input("\nDeseja realizar nova venda? (S/N): ").upper()

print("\nSistema encerrado. Até logo!")

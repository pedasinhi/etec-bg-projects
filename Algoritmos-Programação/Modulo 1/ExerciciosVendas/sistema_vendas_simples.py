while True:

    cliente = input("Digite o nome do cliente: ")
    quantidadeprodutos = int(input("Quantos produtos serão comprados? "))
    if quantidadeprodutos <= 0:
            print("A quantidade deve ser maior que 0")
    else:
        break

    total = 0

    for i in range(quantidadeprodutos):
        print(f"\nProduto {i+1}:")
        nomeproduto = input("Nome do produto: ")
        preco = float(input("Preço do produto: ").replace(",","."))
        if preco <= 0:
            print("O preço deve ser maior que 0")
        else:
            break
        quantidade = int(input("Quantidade: "))
        if quantidade <= 0:
            print("A quantidade deve ser maior que 0")
        else:
            break

        subtotal = preco * quantidade
        print(f"Subtotal de {nomeproduto}: R$ {subtotal:.2f}")

        total += subtotal

    print(f"\nTotal da compra: R$ {total:.2f}")

    if total >= 500:
        desconto = total * 0.10
    elif total >= 200:
        desconto = total * 0.05
    else:
        desconto = 0

    totalfinal = total - desconto

    print("\n--- Resumo da Compra ---")
    print(f"Cliente: {cliente}")
    print(f"Total: R$ {total:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Total final: R$ {totalfinal:.2f}")

    opcao = input("\nDeseja realizar nova venda? (S/N): ").upper()

    if opcao == "N":
        print("Encerrando o sistema...")
        break
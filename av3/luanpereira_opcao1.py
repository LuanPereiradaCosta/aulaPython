print("=" * 40)
print("    Bem vindo ao Lanchonete Python!")

menu = "Cardapio"
pedido = []
valores = []

while True:
    print("=" * 40)
    print(f"{menu:^38}")
    print("=" * 40)
    print("1. Hamburguer -- R$10,00")
    print("2. Refrigerante -- R$05,00")
    print("3. Batata frita -- R$07,00")
    print("4. Nuggets -- R$05,00")
    print("5. Sorvete -- R$03,00")
    print("6. Remover item")
    print("7. Finalizar pedido")
    print("8. Cancelar Pedido")
    print("=" * 40)

    try:
        selecao = int(input("Digite o numero do cardapio: "))
    except ValueError:
        print("Digite apenas numeros.")
        continue

    if selecao == 1:
        lanche = "Hamburguer"
        valor = 10
    elif selecao == 2:
        lanche = "Refrigerante"
        valor = 5
    elif selecao == 3:
        lanche = "Batata frita"
        valor = 7
    elif selecao == 4:
        lanche = "Nuggets"
        valor = 5
    elif selecao == 5:
        lanche = "Sorvete"
        valor = 3

    if 1 <= selecao <= 5:
        pedido.append(lanche)
        valores.append(valor)
        print(f"{lanche} adicionado ao pedido.")
    elif selecao == 6:
        if len(pedido) == 0:
            print("O pedido esta vazio.")
            continue

        while True:
            print("Itens do pedido:")
            for i in range(len(pedido)):
                print(f"{i + 1}. {pedido[i]} -- R$ {valores[i]:.2f}")

            try:
                remover = int(input("Digite o numero do item que voce quer remover: "))
            except ValueError:
                print("Digite apenas numeros.")
                continue

            if 1 <= remover <= len(pedido):
                item_removido = pedido.pop(remover - 1)
                valores.pop(remover - 1)
                print(f"{item_removido} removido do pedido.")
            else:
                print("Este item nao existe no pedido.")

            if len(pedido) == 0:
                print("O pedido esta vazio.")
                break

            remover_outro = str(input("Voce quer remover outro item? [S/N] ")).lower().strip()
            if remover_outro != "s":
                break
    elif selecao == 7:
        if len(pedido) == 0:
            print("O pedido esta vazio.")
            continue

        total = 0
        itens_mostrados = []

        print("Resumo do pedido:")
        for item in pedido:
            if item in itens_mostrados:
                continue

            itens_mostrados.append(item)
            quantidade = pedido.count(item)
            subtotal = 0

            for i in range(len(pedido)):
                if pedido[i] == item:
                    subtotal += valores[i]

            print(f"{quantidade}x {item} -- R$ {subtotal:.2f}")
            total += subtotal

        print(f"Total do pedido: R$ {total:.2f}")
        conf = str(input("Seu pedido esta correto [S/N]: ")).lower().strip()

        if conf == "s" or conf == "sim":
            print("Muito obrigado, seu pedido esta sendo preparado!")
            break
        else:
            print("Voltando ao menu.")
    elif selecao == 8:
        print("Seu pedido foi cancelado!")
        break
    else:
        print("Opcao invalida.")

print("="*40)
print("    Bem vindo ao Lanchonete Python!")
menu = "Cardápio" #só para deixar centralizado a palavra
pedido = []
valores = []
while True:
    print("="*40)
    print(f"{menu:^38}") 
    print("="*40)
    print("1. Hamburguer -- R$10,00")
    print("2. Refrigerante -- R$05,00")
    print("3. Batata frita -- R$07,00")
    print("4. Nuggets -- R$05,00")
    print("5. Sorvete -- R$03,00")
    print("6. Remover item")
    print("7. Finalizar pedido")
    print("8. Cancelar Pedido")
    print("="*40)
    selecao = int(input("Digite o número do cardápio: "))
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
    if selecao <= 5:
        pedido.append(lanche)
        valores.append(valor)
    elif selecao == 6:
        while True:
            cont = 0 
            for p in pedido:
                print(f"{cont}. {p}")
                cont += 1
            remover = int(input("Digite o número correspondente a lista de itens para o item que você quer remover do seu pedido:"))
            pedido.pop(remover)
            valores.pop(remover)
            if remover > 5:
                print("Este número não é um item do cardápio")
            remover_outro = str(input("Você quer remover outro item? [S/N]")).lower()
            if remover_outro != "s":
                break     
    elif selecao == 7:
        for item in set(pedido):
            quantidade = pedido.count(item)
            subtotal = 0

            for i in range(len(pedido)):
                if pedido[i] == item:
                    subtotal += valores[i]

            print(f"{quantidade}x {item} -- R$ {subtotal:.2f}")
            conf = str(input("Seu pedido está correto [S/N]: ")).lower()
            if conf != "n" or conf != "nao":
                print("Muito obrigado, seu pedido está sendo preparado!")
                break
    elif selecao == 8:
        print("Seu pedido foi cancelado!")
        break
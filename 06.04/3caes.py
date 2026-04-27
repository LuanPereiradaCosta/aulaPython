quant = int(input("Digite a quantidade de cães que foram atendidos: "))
if quant < 20:
    print("O petshop ficou Ocioso")
elif quant > 30:
    print("O petshop não aceita mais clientes")
else:
    print("O petshop esta com funcionamento normal")
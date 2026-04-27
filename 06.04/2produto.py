nome = str(input("Digite o nome do produto: "))
quant = int(input("Digite a quantidade do produto: "))
preco = float(input("Digite o preço unitário"))

total_produto = quant * preco
if quant <= 5:
    desc = 0.98
elif 5 < quant <= 10:
    desc = 0.97
else:
    desc = 0.95

total = total_produto * desc

print(f"total a pagar: {total}")


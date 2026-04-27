'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool: 
até 20 litros, desconto de 3% por litro
e acima de 20 litros, desconto de 5% por litro; 

Gasolina: 
até 20 litros, desconto de 4% por litro 
e acima de 20 litros, desconto de 6% por litro. 

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (A-álcool, G-gasolina) e imprima o valor a ser pago pelo cliente.

Considere que o preço do litro da gasolina é R$ 6,89 e o preço do litro do álcool
é R$ 4,89.'''

litros = int(input("Quantos litros: "))
comb = str(input("Alcool ou Gasolina [A/G]: ")).lower().strip()
if comb == "g":
    valor_gasolina = litros*6.89
    if litros <= 20:
        final = valor_gasolina*0.96
    else:
        final = valor_gasolina*0.94

elif comb == "a":
    valor_alcool = litros*4.89
    if litros <= 20:
        final = valor_alcool*0.97
    else:
        final = valor_alcool*0.95
print(f"O valor fica: {final:.2f}")
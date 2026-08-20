'''Um banco concedera um credito especial aos seus clientes, variavel com o saldo
medio no ultimo ano. Faca um algoritmo que leia o saldo medio de um cliente e
calcule o valor do credito de acordo com a tabela abaixo. Mostre uma mensagem
informando o saldo medio e o valor do credito.
Saldo medio Percentual
de 0 a 200 nenhum credito
de 201 a 400 20% do valor do saldo medio
de 401 a 600 30% do valor do saldo medio
acima de 601 40% do valor do saldo medio'''

saldo_medio = float(input("Qual o saldo medio: R$ "))

if saldo_medio < 0:
    print("Saldo medio invalido.")
else:
    if saldo_medio <= 200:
        credito = 0
    elif saldo_medio <= 400:
        credito = saldo_medio * 0.20
    elif saldo_medio <= 600:
        credito = saldo_medio * 0.30
    else:
        credito = saldo_medio * 0.40

    print(f"Saldo medio: R$ {saldo_medio:.2f}")
    print(f"Credito calculado: R$ {credito:.2f}")

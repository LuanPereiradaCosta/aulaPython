altura = float(input("Digite altura: "))
peso = float(input("Digite peso: "))
imc = peso/altura**2
print(f"Imc: {imc}")
if imc < 18.5:
    print("Abaixo do peso normal")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Excesso de Peso")
elif 30 <= imc < 35:
    print("Obesidade classe 1")
elif 30 <= imc < 40:
    print("Obesidade classe 2")
else:
    print("Obesidade classe 3") 
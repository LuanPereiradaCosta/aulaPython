horas_trabalhadas = int(input("Quantas horas-aula o professor trabalha? "))

print("Selecione o nível do professor:")
print("[1] Nível 1")
print("[2] Nível 2")
print("[3] Nível 3")

nivel = int(input("Nível: "))

if nivel == 1:
    valor_hora = 12
elif nivel == 2:
    valor_hora = 17
elif nivel == 3:
    valor_hora = 25
else:
    valor_hora = 0
    print("Esse nível não existe.")

if valor_hora > 0:
    salario = horas_trabalhadas * valor_hora
    print(f"O salário do professor será de R$ {salario:.2f}")
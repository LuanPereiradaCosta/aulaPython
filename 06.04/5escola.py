hora = int(input("Quantas horas aula o professor trabalha: "))
print("Selecione o nivel do professor: ")
print("[1]\n[2]\n[3]")
nivel = input( ":")

if nivel == 1:
    aula = 12
elif nivel == 2:
    aula = 17
elif nivel == 3:
    aula = 25
else:
    print("Esse nivel não existe")

salario = hora*aula

print(f"O salario do professor vai ser: {salario}")
'''Tendo como dados de entrada:
● a altura
● e o sexo de uma pessoa (M masculino e F feminino)
Construa um algoritmo que calcule seu peso ideal, utilizando as seguintes
fórmulas:
● para homens: (72.7*h)-58
● para mulheres: (62.1*h)-44.7'''

altura = float(input("Digite altura:"))
sexo = str(input("Digite o sexo[M/F]")).upper().strip()


if sexo == "M":
    altM = (72.7*altura) - 58
    print(f"O peso ideal para sua altura é {altM}")
elif sexo == "M":
    altF = (62.1*altura) - 44.7
    print(f"O peso ideal para sua altura é {altF}")
else:
    print("Valor invalido no seu sexo")
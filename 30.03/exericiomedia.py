nome = str(input("Digite seu nome: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print("Notas informadas estao incorretas!")
else:
    media = (nota1 + nota2) / 2

    if media >= 7:
        print(f"O aluno {nome} com a nota {media:.2f} esta Aprovado!")
    elif media >= 4:
        print(f"O aluno {nome} com a nota {media:.2f} esta de Recuperacao!")
    else:
        print(f"O aluno {nome} com a nota {media:.2f} esta Reprovado!")

nome = str(input("Digite seu nome: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if 10 >= media >= 7:
    print(f"O aluno {nome} com a nota {media} está Aprovado!")
elif 4 <= media < 6:
    print(f"O aluno {nome} com a nota {media} está de Recuperação!")
elif 4 > media > 0:
    print(f"O aluno {nome} com a nota {media} está Reprovado!")
else:
    print("Notas informadas estão incorretas!")

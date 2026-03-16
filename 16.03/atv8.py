anoNascimento = int(input('Digite o seu ano de nascimento: '))
anoAtual = int(input('Digite o ano atual: '))
anos = anoAtual - anoNascimento
dias = anos * 365
meses = anos * 12
semanas = anos * 48
print(f'Sua idade em anos: {anos} meses: {meses} semanas: {semanas} dias: {dias}')
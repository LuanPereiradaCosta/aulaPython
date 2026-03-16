salario = float(input("Digite o salario fixo: "))
vendas = float(input("Digite o número de vendas: "))
comissao = vendas*0.04
total = salario + comissao
print(f'O salário do funcionário com a comissao fica: {total}, salário: {salario}, comissão: {comissao}')


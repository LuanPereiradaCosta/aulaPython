normal_hora = float(input('Quantas horas normais trabalhadas: '))
extra_hora = float(input('Quantas horas extras trabalhadas: '))
normal = normal_hora*10
extra = extra_hora*15
bruto = normal+extra
liquido = bruto*0.90
print(f'O salário do funcionario que trabalhou {normal_hora} horas normais e {extra_hora} horas extras')
print(f'Fica com o salário bruto R${bruto} e o salário liquido R${liquido}')
print(f'Com cada fora valendo -> normal: R${normal} e extra: R${extra}')

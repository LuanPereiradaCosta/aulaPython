conta = float(input('Qual o valor da conta: '))
valor_inteiro = int(conta//3) #ja que carlos e andre pagam a conta sem os centavos, se pega apenas a parte inteira com //
carlos = valor_inteiro
andre = valor_inteiro 
felipe = conta-andre-carlos #normal e diminuir com carlos e andre q não pagam centavos 
print(f'Carlos: {carlos:.2f}\nAndré: {andre:.2f}\nfelipe: {felipe:.2f}')
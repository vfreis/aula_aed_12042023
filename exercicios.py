import json, jsonify, math
# I - Faça um código que pergunte a nota das quatro avaliações de uma disciplina e calcule a média aritimética dessas notas.

def ex1():
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    return ((a + b + c + d) / 4)
# print(media())

# II - Faça um código que pergunte seu nome, idade, profissão e esporte preferido e depois liste 

def ex2():
    nome = str(input("Qual seu nome?\n"))
    idade = str(input("Qual sua idade?\n"))
    profissao = str(input("Qual sua profissão?\n"))
    esporte = str(input("Qual seu esporte favorito?\n"))
    # return(f'Nome = {nome}\n'  f'Idade = {idade}\n' f'Profissao =  {profissao}\n' f'Esporte Favorito = {esporte}')
    resposta = f'"nome": {nome},"idade": {idade},"profissao": {profissao},"esporte": {esporte}'
    # dump = json.dumps(resposta)
    return (resposta)

# print(ex2())

# III - Faça um algoritmo onde o usuário entre com a cotação do dolar do dia e converta um dado valor em real para dolar.
def ex3():
 moeda = float(input("informe valor atual da moeda"))
 valor = float(input('digite quantos reais (BRL R$)'))
 resultado = valor / moeda
 return f'seus R${valor} compram US${resultado:.2f}'

# IV - Faça um algoritmo onde o usuário entre com o valor de uma mercadoria e a taxa de desconto, Exiba o percentual de desconto e o valor a ser pago pelo cliente.
def ex4():
    valor = float(input('Digite o valor da mercadoria \n'))
    desconto = float(input('Informe o desconto\n'))
    if desconto > 100:
        return 'desconto acima do permitido'
    else:
        resultado = (valor * desconto/100)
        subtotal = valor - resultado
        return f'o valor do desconto é R${resultado} e o valor final da mercadoria é R${subtotal}'

# V - Elabore um algoritmo que peça ao usuário que entre com dois números e depois imprima na tela a soma, subtração, multiplicação e raiz quadrada dos dois números, exibir a raiz quadrada com 4 casas decimais
def ex5():
    valor1 = float(input('digite valor 1\n'))
    valor2 = float(input('digita valor 2 \n'))
    soma = valor1 + valor2
    subtraçao = valor1 - valor2
    multiplicacao = valor1 * valor2
    r_v1 = math.sqrt(valor1)
    r_v2 = math.sqrt(valor2)
    return f'Soma: {soma} Subtração: {subtraçao} \nMultiplicação: {multiplicacao} \nRaiz valor1 {r_v2}\n Raiz valor2: {r_v1}'

# VI - Dado dois números inteiros determine o valor da divisão, a parte inteira e o resto da divisão
def ex6():
    valor1 = float(input('digite valor1'))
    valor2 = float(input('digite valor2'))
    quociente = valor1 / valor2
    resto = valor1 % valor2
    return f'quociente v1/v2: {quociente} resto valor1%valor2: {resto}'

# VII - Peça para o aluno digitar seu RA e depois imprima apenas os dois últimos algarismos do RA
def ex7():
    ra = str(input('digite seu Registro de Aluno:'))
    final = ra[-3:]
    return f'RA: {ra} 3 ultimos: {final}'

# VIII - Elabore um algoritmo que peça para o aluno fornecer as 4 melhores notas das ACs, as 3 notas PAI e a nota da avaliação final e calcule sua nota final.
def ex8():
    pass








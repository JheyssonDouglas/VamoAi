# Descrição
# Nesta atividade você vai criar uma função que vai imitar uma calculadora simples.

# A função deve receber dois números e uma operação aritmética(+, -, *, /) como string e deve retornar o resultado desta operação.

# Instruções
# Crie uma variável chamada primeiro_numero e atribua o número qualquer.
# Crie uma variável chamada segundo_numero e atribua o número qualquer.
# Crie uma variável chamada operador e atribua uma das operações aritméticas como string.
# Crie uma função chamada minha_calculadora que recebe 3 argumentos:
# a: o primeiro número
# b: o segundo número
# operador: a operação aritmética
# Dentro da função, implemente uma lógica que verifica qual operador a função recebeu retorne o resultado da operação correta.
# IMPORTANTE: Se o operador não existir, deve-se retornar o valor 999999999, que corresponde a um erro na operação.

def minha_calculadora(a, b, operador):
    if operador == "+":
        resultado = a + b
    elif operador == "-":
        resultado = a - b
    elif operador == "*":
        resultado = a * b
    elif operador == "/":
        resultado = a / b
    else:
        resultado = 999999999
    return resultado


primeiro_numero = 99
segundo_numero = 7
operador = "+"

minha_calculadora(99, 7, "+")
print(minha_calculadora(99, 7, "+"))

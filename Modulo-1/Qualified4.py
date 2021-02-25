# Descrição
# Nesta atividade você vai criar uma função que recebe um número inteiro e verifica se ele é negativo ou não.

# A função deve retornar um valor booleano.

# Instruções
# Crie uma variável chamada numero_inteiro e atribua um valor inteiro à ela. Lembre-se que pode ser negativo ou positivo.
# Crie uma função chamada sera_que_e_negativo que recebe um argumento numero_inteiro.
# Dentro da função, implemente uma lógica para verificar se a variável numero_inteiro representa um inteiro negativo ou não.
# A função deve retornar um valor booleano como resultado.
# 5 - Complete a função
# def nome_da_funcao(argumento):
# Implemente aqui a lógica da funcao
# 5 - Complete a função
# def nome_da_funcao(argumento):
# Implemente aqui a lógica da funcao
# 4 -Complete a função
# def nome_da_funcao(argumento):
# Implemente aqui a lógica da funcao
def sera_que_e_negativo(numero_inteiro):
    if numero_inteiro <= -1:
        resultado = True
    elif numero_inteiro >= 0:
        resultado = False
    return resultado


numero_inteiro = -71
resultado = bool(numero_inteiro)

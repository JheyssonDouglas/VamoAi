# Descrição
# Nesta atividade você vai criar uma função que implementa o que foi feito na atividade Dia da semana.

# Crie uma função que identifica qual é o dia da semana correspondente aos números de 1 a 7.

# Lembrar: A semana começa no domingo e termina sábado

# Os valores para os dias da semana DEVEM ser:

# Domingo
# Segunda
# Terça
# Quarta
# Quinta
# Sexta
# Sábado
# Caso o número da semana não esteja entre 1 e 7, deve-se retorna a string vazia "".

# Instruções
# Crie uma variável chamada numero_dia_semana e atribua um número inteiro à ela de 1 a 7.
# Cria uma função chamada de qual_o_nome_do_dia() que recebe o número correspondente ao dia da semana e retorna o seu nome correspondente.
# Ao final utilize a função print() para verificar o resultado.
# 7 - Calcular dia da semana

numero_dia_semana = 3
nome_dia_semana = ""

# Implementa aqui a lógica condicional para atribuir o nome do dia da semana correto
if (numero_dia_semana == 1):
    nome_dia_semana = "Domingo"
elif (numero_dia_semana == 2):
    nome_dia_semana = "Segunda"
elif (numero_dia_semana == 3):
    nome_dia_semana = "Terça"
elif (numero_dia_semana == 4):
    nome_dia_semana = "Quarta"
elif (numero_dia_semana == 5):
    nome_dia_semana = "Quinta"
elif (numero_dia_semana == 6):
    nome_dia_semana = "Sexta"
elif (numero_dia_semana == 7):
    nome_dia_semana = "Sábado"
else:
    nome_dia_semana = ""

print(nome_dia_semana)


numero_dia_semana = 1
nome_dia_semana = ""

# Implementa aqui a lógica condicional para atribuir o nome do dia da semana correto


def qual_o_nome_do_dia(numero_dia_semana):
    if (numero_dia_semana == 1):
        nome_dia_semana = "Domingo"
    elif (numero_dia_semana == 2):
        nome_dia_semana = "Segunda"
    elif (numero_dia_semana == 3):
        nome_dia_semana = "Terça"
    elif (numero_dia_semana == 4):
        nome_dia_semana = "Quarta"
    elif (numero_dia_semana == 5):
        nome_dia_semana = "Quinta"
    elif (numero_dia_semana == 6):
        nome_dia_semana = "Sexta"
    elif (numero_dia_semana == 7):
        nome_dia_semana = "Sábado"
    else:
        nome_dia_semana = ""
    return nome_dia_semana


nome_dia_semana = qual_o_nome_do_dia(numero_dia_semana)
print(nome_dia_semana)

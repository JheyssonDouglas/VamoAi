# Descrição
# Nesta atividade você irá criar uma função que recebe a idade de uma pessoa e retorna sua idade em dias.

# Regras importantes:

# A idade não pode ser menor que 0
# A idade não pode ser maior que 120
# Se a idade não cair dentro do intervalo aceitável pelas regras anteriores, a função deve retornar -1
# Lembrar: 1 ano = 365 dias

# Instruções
# Crie uma função chamada calcula_idade_em_dias() que recebe a idade como parâmetro.
# Implemente a lógica da função para calcular a idade em dias e retornar seu valor.
# Utilize a função print() para imprimir o valor retornado pela função.

def calcula_idade_em_dias(idade):
    idade_em_dias = idade * 365
    if (idade < 0) or (idade > 120):
        return -1
    else:
        return idade_em_dias


idade = 1

calcula_idade_em_dias(idade)
print(calcula_idade_em_dias(idade))
# Implemente aqui a lógica da função

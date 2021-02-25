# Descrição
# Nesta atividade você vai criar um programa que identifica a classe eleitoral de uma pessoa a partir de sua idade.

# Para definir isso basta seguir as seguintes regras:

# Abaixo de 16 anos : Não Eleitor
# Entre 18 e menor de 65 anos: Eleitor Obrigatório
# De 16 a 18 e maior de 65: Eleitor Facultativo
# Instruções
# Crie uma variável chamada idade e atribua um número inteiro à ela.
# Implemente uma sequência lógica condicional para definir qual a classe eleitoral da pessoa a partir da variável idade. A classe eleitoral deve ser atribuída à uma variável chamada de classe_eleitoral
# Ao final utilize a função print() para verificar o resultado.

idade = 26
classe_eleitoral = "Eleitor Obrigatório"
# Insira aqui a lógica para definir a classe eleitoral
if idade > 16 and idade < 18 or idade > 65:
    print(classe_eleitoral)

elif idade >= 18 and idade <= 65:
    print("Eleitor Obrigatório")

else:
    print(classe_eleitoral)

# print no resultado

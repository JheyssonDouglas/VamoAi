resposta = int(input("Qual a sua idade? "))

if resposta <= 12:
    print("Você é uma criança!")
elif resposta > 13 and resposta <= 18:
    print("Você é um adolescente!")
elif resposta >= 19 and resposta <= 59:
    print("Você é um adulto!")
else:
    print("Você é um idoso!")

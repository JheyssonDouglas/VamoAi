nome = str(input("Qual o seu nome? "))
print(nome, "informe por gentileza o nome de três produtos de mercado e,\n"
      "seus respectivos preços?")

produto1 = str(input("Primeiro produto: "))
preco1 = float(input("Qual o preço? "))
produto2 = str(input("Segundo produto: "))
preco2 = float(input("Qual o preço?"))
produto3 = str(input("Terceiro produto: "))
preco3 = float(input("Qual o preço? "))

if preco1 < preco2 and preco1 < preco3:
    print("O", produto1, "é o mais barato!")

elif preco2 < preco1 and preco2 < preco3:
    print("O", produto2, "é o mais barato!")

else:
    print("O", produto3, "é o mais barato!")

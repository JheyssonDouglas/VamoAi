print("1. São Paulo")
print("2. Palmeiras")
print("3. Corinthians")
print("4. Santos")

resposta = int(input("Você torce para: "))

if resposta == 1 or resposta == 3 or resposta == 4:
    print("Parabéns, você tem mundial!")
elif resposta == 2:
    print("Que pena, você não tem mundial!")
else:
    print("Código inválido")

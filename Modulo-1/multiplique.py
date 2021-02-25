print("Você só pode escolher um número entre 1 e 50!")


def pula_linha():
    print("")


pula_linha()


def numero(primeiro_numero, segundo_numero):
    numero = (primeiro_numero * segundo_numero)
    print(numero)


primeiro_numero = int(input("Qual o primeiro número? "))
segundo_numero = int(input("Qual o segundo número? "))

numero(primeiro_numero, segundo_numero)

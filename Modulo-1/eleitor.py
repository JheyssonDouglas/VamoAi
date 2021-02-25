idade = 30
# Insira aqui a lógica para definir a classe eleitoral


def classe_eleitoral(não_eleitor, eleitor_obrigatório, eleitor_facultativo):
    if idade < 16:
        print("Não eleitor")

    elif idade >= 18 and idade <= 65:
        print("Eleitor Obrigatório")

    else:
        print("Eleitor Facultativo")

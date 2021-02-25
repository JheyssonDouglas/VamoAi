def comparar_idade(idade_jheysson, idade_valerie_thomas):
    comparar_idade = (idade_valerie_thomas - idade_jheysson)
    print("Jheysson e Valerie Thomas tem uma diferença de idade de",
          comparar_idade, "anos entre os dois!")


def comparar_cidade(cidade_jheysson, cidade_valerie_thomas):
    comparar_cidade = (cidade_jheysson, cidade_valerie_thomas)
    print("Jheysson mora em", cidade_jheysson, "e Valerie Thomas mora em",
          cidade_valerie_thomas, ", por tanto, ambos moram em cidades diferentes!")


def comparar_pais(pais_jheysson, pais_valerie_thomas):
    comparar_pais = (pais_jheysson, pais_valerie_thomas)
    print("Jheysson é natural do", pais_jheysson,
          " e Valerie thomas é natural dos", pais_valerie_thomas, "!")


print("Segue comparação entre Jheysson e Valerie Thomas")
comparar_idade(30, 78)
comparar_cidade("Goiânia-GO", "Maryland-Estados Unidos da America")
comparar_pais("Brasil", "Estados Unidos da America")

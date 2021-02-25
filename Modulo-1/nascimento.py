def idade(ano_final, ano_inicial):
    idade = (ano_final - ano_inicial)
    print(idade)


ano_final = int(input("Em que ano estamos? "))
ano_inicial = int(input("Qual ano você nasceu? "))

idade(ano_final, ano_inicial)

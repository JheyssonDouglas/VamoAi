nome = str(input("Qual o seu nome? "))
idade = int(input("Qual sua idade? "))

menor = 18 - idade

def pula_linha():
    print("")
    
if idade >= 18:
    pula_linha()
    print("Você é estudante de PYTHON?")
    print("[1] SIM")
    print("[2] NÃO")
   
    resposta = int(input("Você escolheu: "))
    pula_linha()
    
    if resposta == 1:
        print(nome,"Parabéns, você acaba de ganhar 50% de desconto no seu ingresso!")
    print("Escolha entre duas opções:")
    print("[1] Ingresso Padrão: R$17,50")
    print("[2] Ingresso Vip: R$ 30,00")
    pula_linha()
    if resposta == 2:
        print(nome, "Você tem duas opções de ingresso:")
        print("Escolha o seu ingresso?")
        print("[1] Ingresso Padrão: R$35,00")
        print("[2] Ingresso Vip: R$ 60,00")
    
    resposta1 = int(input("Você escolheu: "))

    if resposta == 1 or resposta == 2:
        print("Seja bem vindo!")
       
else:
    print("Desculpe",nome,"você ainda é menor de idade e por isso não posso liberar sua entrada.\n"
    "Mas daqui", menor, "ano(s), você poderá entrar!")

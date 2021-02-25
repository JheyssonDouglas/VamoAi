aluno1 = float(input("Qual a média do primeiro aluno: "))
aluno2 = float(input("Qual a média do segundo aluno: "))
aluno3 = float(input("Qual a média do terceiro aluno: "))
aluno4 = float(input("Qual a média do quarto aluno: "))
aluno5 = float(input("Qual a média do quinto aluno: "))

media = (aluno1 + aluno2 + aluno3 + aluno4 + aluno5) / 5

print("A média entre os 5 alunos é de", media)

if media >= 7 and media <= 10:
    print("Parabéns, os alunos estão com uma média boa!")

if media >= 4 and media < 7:
    print("Os alunos precisam melhorar pois estão com a média mediana!")

if media < 4:
    print("A média dos alunos esta abaixo do esperado, precisam melhorar urgente!")

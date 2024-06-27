nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("A sua média é ", media)

if media >= 70:
    print("Aprovado")
if media >= 50 and media <= 69:
    print("Recuperação")
if media < 50:
    print("Reprovado")
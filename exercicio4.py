salario = int(input("Qual o seu salário? "))

if salario < 281:
    print("O seu salário era ", salario)
    print("O aumento do seu salário será de 20%")
    reajuste1 = (salario * 1.2) - salario 
    print("O aumento do seu salário será de ", reajuste1)
    print("O seu salário com o reajuste será de", salario * 1.2)

elif salario >= 281 and salario < 702:
    print("O seu salário era ", salario)
    print("O aumento do seu salário será de 15%")
    reajuste2 = (salario * 1.15) - salario 
    print("O aumento do seu salário será de ", reajuste2)
    print("O seu salário com o reajuste será de", salario * 1.15)

elif salario >= 702 and salario <= 1500:
    print("O seu salário era ", salario)
    print("O aumento do seu salário será de 10%")
    reajuste3 = (salario * 1.1) - salario 
    print("O aumento do seu salário será de ", reajuste3)
    print("O seu salário com o reajuste será de", salario * 1.1)

elif salario > 1501:
    print("O seu salário era ", salario)
    print("O aumento do seu salário será de 5%")
    reajuste4 = (salario * 1.05) - salario 
    print("O aumento do seu salário será de ", reajuste4)
    print("O seu salário com o reajuste será de", salario * 1.05)
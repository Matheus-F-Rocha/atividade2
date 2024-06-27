lado1 = int(input("Digite a medida do primeiro lado: "))
lado2 = int(input("Digite a medida do segundo lado: "))
lado3 = int(input("Digite a medida do terceiro lado: "))

if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("Triângulo escaleno")

elif lado1 == lado2 and lado1 == lado3:
    print("Triângulo equilátero")

elif lado1 == lado2 or lado1 != lado3 and lado1 != lado2 and lado2 == lado3 or lado1 != lado2 and lado1 == lado3:
    print("Triângulo isósceles")

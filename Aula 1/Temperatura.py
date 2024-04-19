a = float(input("Digite o comprimento do primeiro lado do triangulo: "))
b = float(input("Digite o comprimento do segundo lado do triangulo: "))
c = float(input("Digite o comprimento do terceiro lado do triangulo: "))
if a==b==c:
    print("Esse triangulo é equilatero!")
elif a!=b!=c!=a:
    print("Esse triangulo é escaleno!")
else:
    print("Esse triangulo é isósceles")
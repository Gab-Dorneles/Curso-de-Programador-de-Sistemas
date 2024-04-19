a=float(input("Informe o primeiro lado do seu triangulo: "))
b=float(input("Informe o segundo lado do seu triangulo: "))
c=float(input("Informe o terceiro lado do seu triangulo: "))
if a==b==c:
    print("O triangulo é Equilatero!")
elif a!=b!=c!=a:
    print("O triangulo é Escaleno!")
else:
    print("O triangulo é Isóseles!")

numero = int(input("Digite um numero de 1 a 10: "))

if 1 <= numero <= 10:
    for i in range(1,11):
        print(numero,"x", i,"=",numero*i)
else:
    print("Tabuada somente até o 10")
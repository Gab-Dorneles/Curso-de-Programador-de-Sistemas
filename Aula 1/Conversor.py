print("1- Converter de Celsius para Fahrenheit: ")
print("2- Converter Fahreneit para Celsius: ")
opcao=int(input("Escolha o tipo de conversão 1 ou 2: "))
match opcao:

 case 1:
    celcius=float(input("Escolha sua temperatura em Celcius: "))
    print("A temperatura em Fahrenhit é: ",(celcius*9/5)+32)
 case 2:
    fahrenheit=float(input("Escolha sua temperatura em Fahrenhit: "))
    print("A temperatura em Celsius é: ",(fahrenheit-32)*5/9)
 case _:
    print("Opção Inválida")

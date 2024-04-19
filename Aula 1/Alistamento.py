sexo=input("Digite seu sexo (M para masculino ou F para feminino): ")
altura= float(input("Digite sua altura em metros: "))

if sexo == 'm':
    if altura >= 1.70:
        print("Você está apto!")
    else:
        print("Você não está apto!")
elif sexo =='f':
    if altura >= 1.60:
        print("Você está apta!")
    else:
        print("Você não está apta!")



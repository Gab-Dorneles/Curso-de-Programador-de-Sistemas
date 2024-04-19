nome = (input("Digite seu nome: "))
while len (nome) < 3:
    print("Informe um nome com mais de 3 letras! ")
    nome = (input("Digite seu nome novamente: "))
idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    print("Informe um valor valido")
    idade = int(input("Digite sua idade novamente: "))
salario = float(input("Digite seu Salário: "))
while salario < 0:
    print("O salario não pode ser menor que 0")
    salario = float(input("Digite Seu Salário Novamente: "))
sexo = (input("Digite seu sexo (f/m): "))
while sexo != "f" and sexo != "m":
    print("Informe 'f' feminino 'm' masculino ")
    sexo = (input("Digite seu sexo novamente:(c,s,v,d) "))
estado = (input("Digite seu Estado Civil:  "))
while estado != "s" and estado != "c" and estado != "v" and estado != "d":
    print("Digite estado civil inválido: ")
    estado = (input("Digite seu Estado civil: "))

print("Fim do Formulario")

    
   
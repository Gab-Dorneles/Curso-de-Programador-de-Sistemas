num = int(input("Digite um número: "))
maior = num
for num in range (4):
    num = int(input("Digite um número: "))
    if num > maior:
        maior = num
print(maior)
print("Esse é o Número Maior! ")
manga = int(input("Informe a quantidade de Mángas na Coleção: "))
total = 0
for i in range(manga):
    valor = float(input("Informe o Valor dos Mángas: "))
    total += valor
    
print("O total é: ",total)
media = total / manga
print("A média é: ", media)
    
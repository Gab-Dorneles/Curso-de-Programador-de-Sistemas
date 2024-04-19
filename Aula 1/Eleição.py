eleitor = int(input("Digite a quantidade de candidatos: "))
print("2101- Tião do Gás 2403-Shaolin Matador de Porco 1202-Zé da Manga")
tiao=0
porco=0
zedamanga=0

for i in range(eleitor):
    voto = int(input("Coloque o número seu candidato: "))
    if voto == 2101:
        tiao += 1
    elif voto == 2403:
        porco += 1
    elif voto == 1202:
        zedamanga += 1 
    else:
        print("O voto foi inválido.")
print("A quantidade de votos do 2101- Tião do Gás foi: ",tiao)
print("A quantidade de votos do 2403- Shaolin Matador de Porco foi: ",porco)
print("A quantidade de votos do 1202- Zé da Manga foi: ",zedamanga)


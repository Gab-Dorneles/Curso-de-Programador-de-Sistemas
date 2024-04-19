turno=(input("Solicite seu turno de Trabalho: "))

match turno:

 case "m":
    print("Matutino")
    print("Bom dia!")
 case "v":
    print("Vespertino")
    print("Boa Tarde!")
 case "n":
    print("Noturno")
    print("Boa Noite!")
 case _:
      print("Opcão Invalida")
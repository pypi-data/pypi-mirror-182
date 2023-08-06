import json
def ImprimirMenu():
    print("/****** MENU ******/")
    print("1) Añadir Digimon a Lista ")
    print("2) Almacenar Digimones en Fichero")
    print("3) Leer lista Digimones  ")
    print("4) Ver lista Digimones ")

def Introducirdigimons(ListaDigimons):
    continuar=""
    while continuar!="N":
        digimon={"nombre":"", "tipo":"", "nivel":"", "ataque":"", "defensa":""}
        digimon["nombre"]=( input("Introduce Nombre: ").capitalize())
        while True:
            digimon["tipo"]=( input("Introduce Tipo (vacuna, virus, animal, planta, elemental): "))
            if digimon["tipo"] not in ["vacuna", "virus", "animal" , "planta" , "elemental"]:
                print("Valor no valido")
            else:
                break
        while True:
            digimon["nivel"]=( int(input("Introduce Nivel: ").capitalize()))
            if digimon["nivel"]<0:
                print("Valor no valido")
            else:
                break
        while True:
            digimon["ataque"]=( int (input("Introduce Ataque: ")))
            if digimon["ataque"]<0:
                print("Valor no valido")
            else:
                break
        while True:
            digimon["defensa"]=( int (input("Introduce Defensa: ")))
            if digimon["defensa"]<0:
                print("Valor no valido")
            else:
                break
        ListaDigimons.append(digimon)
        print("Digimon Dado de alta correctamente")
        print (ListaDigimons)
        continuar=input ("¿Quieres continuar añadiendo? S/N: ").upper()

def VerDigimons(ListaDigimons):
    for indice, digimon, in enumerate(ListaDigimons):
        print (f"/***Datos Digimon {indice+1}***/")
        print (f"nombre: {digimon['nombre']}")
        print (f"tipo: {digimon['tipo']}")
        print (f"nivel: {digimon['nivel']}")
        print (f"ataque: {digimon['ataque']}")
        print (f"defensa: {digimon['defensa']}")
        print()

def AlmacenarDigimon(ListaDigimons):
    with open ("digimons.json", "w") as fichero:
        json.dump(ListaDigimons,fichero)

def LeerDigimons(ListaDigimons):
    with open ("digimons.json", "r") as fichero:
        return json.load(ListaDigimons)

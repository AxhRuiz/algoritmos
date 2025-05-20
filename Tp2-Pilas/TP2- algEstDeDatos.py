
# EJERCICIO 13

print(f"INICIO EJERCICIO 13")

def trajes_iron_man(modelo, pelicula, estado):
    return {
        "modelo": modelo,
        "pelicula" : pelicula,
        "estado": estado
    }

lista_trajes = []
lista_trajes.append(trajes_iron_man("MARK IV", "IRON MAN 1", "DAÑADO"))
lista_trajes.append(trajes_iron_man("MARK VII", "THE AVENGERS", "IMPECABLE" ))
lista_trajes.append(trajes_iron_man("MARK XLII", "IRON MAN 3", "DESTRUIDO"))
lista_trajes.append(trajes_iron_man("MARK XLIV", "AVENGERS: AGE OF ULTRON", "IMPECABLE" ))
lista_trajes.append(trajes_iron_man("MARK XLVI", "CAPTAIN AMERICA: CIVIL WAR", "DAÑADO"))

 # ITEM A 
print(f"ITEM A")  
for trajes in lista_trajes:
    if  trajes["modelo"] == "MARK XLIV":
        print("El traje se encuentra en la lista y estuvo en la pelicula: " + trajes["pelicula"])
   
# ITEM B
print("ITEM B")
for trajes in lista_trajes:
    if trajes["estado"] == "DAÑADO":
        print("Los datos de los trajes dañados son: " + "TRAJE: " + trajes["modelo"] + "- PELICULA: " + trajes["pelicula"] + "- ESTADO: "+ trajes["estado"] )
# ITEM C
print(f"ITEM C")
for i in range(len(lista_trajes) -1, -1 , -1):
    if lista_trajes[i]["estado"] == "DESTRUIDO":
        traje_eliminado = lista_trajes.pop(i)
        print("El traje que será eliminado de la lista por el estado en el que se encuentra es: " + traje_eliminado["modelo"])

print(f"ITEM E")
existe = any(t["modelo"] == "MARK LXXXV" and t["pelicula"] == "AVENGERS: ENDGAME" for t in lista_trajes)
if not existe:
    lista_trajes.append(trajes_iron_man("MARK LXXXV", "AVENGERS: ENDGAME", "IMPECABLE"))

lista_trajes.append(trajes_iron_man("MARK XLVI", "SPIDER MAN: HOMECOMING", "IMPECABLE"))


print(lista_trajes)

print(f"ITEM F")
trajes_peliculas = ["SPIDER MAN: HOMECOMING", "CAPTAIN AMERICA: CIVIL WAR"]

for trajes in lista_trajes:
    if trajes["pelicula"] in trajes_peliculas:
        print("El traje utilizado en una de las peliculas es nombradas es: " "  TRAJE: "+ trajes["modelo"] + "  PELICULA: " + trajes["pelicula"])




#EJERCICIO 24

print(f"INICIO EJERCICIO 24")

def lista_personajes(nombre, peliculas):
    return {
        "nombre" : nombre,
        "peliculas" : peliculas
    }

personajes_marvel = []
personajes_marvel.append(lista_personajes("Iron Man", 10))
personajes_marvel.append(lista_personajes("Capitan America", 9))
personajes_marvel.append(lista_personajes("Thor", 7))
personajes_marvel.append(lista_personajes("Black Widow", 6))
personajes_marvel.append(lista_personajes("Hulk", 7))
personajes_marvel.append(lista_personajes("Spider Man", 7))
personajes_marvel.append(lista_personajes("Scarlet witch", 4))
personajes_marvel.append(lista_personajes("Rocket Raccon", 3))
personajes_marvel.append(lista_personajes("Groot", 2))

print(personajes_marvel)

print(f"ITEM A")
for personaje in range(len(personajes_marvel) -1, -1, -1):
    if personajes_marvel[personaje]["nombre"] == "Rocket Raccon" or personajes_marvel[personaje]["nombre"] == "Groot":
        posicion = len(personajes_marvel) -personaje
        print(f"{personajes_marvel[personaje]["nombre"]} esta en la posicion:  {posicion}")
            
print("ITEM B")
for personaje in personajes_marvel:
    if personaje["peliculas"] > 5:
        print(f" la cantidad de peliculas en las que actuo {personaje["nombre"]} es de: {personaje["peliculas"]}")

print(f"ITEM C")
for personaje in personajes_marvel:
    if personaje["nombre"] == "Black Widow":
        print(f"las peliculas en las que participo {personaje["nombre"]} fueron: {personaje["peliculas"]}")

print(f"ITEM D")
for personaje in personajes_marvel:
    if personaje["nombre"].startswith(("C", "D", "G")):
        print(f"Los nombres de los personajes cuyos nombres empiezan con C, D o G son: {personaje["nombre"]}")
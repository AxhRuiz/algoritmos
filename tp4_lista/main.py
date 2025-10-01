from List import List
from Jedis import jedis
from super_heroes_data import superheroes

superHeroes1 = List()

for heroe in superheroes:
    superHeroes1.append(heroe) 


print("\n")
def order_by_name(item):
    return item["alias"]

superHeroes1.add_criterion("alias", order_by_name)

superHeroes1.sort_by_criterion("alias")



# a- eliminar el nodo que contiene la información de Linterna Verde;

print("\n")
print("eliminar a Linterna Verde")
eliminado = superHeroes1.delete_value("Linterna Verde", "alias")
print(f"el eliminado es: {eliminado}")



#mostrar el año de aparición de Wolverine;

buscado = superHeroes1.search("Wolverine", "alias")

if buscado is not None:
    wolverine = superHeroes1[buscado]
    print(f"Wolverine aparecio en el año", {wolverine["first_appearance"]})
else:
    (f"No se encontró a wolverine")

#cambiar la casa de Dr. Strange a Marvel;
print("\n")
buscado1 = superHeroes1.search("Dr Strange", "alias")

if buscado1 is not None:
    nueva_casa = "Marvel"
    superHeroes1[buscado1]["house"] = nueva_casa
    print(f"La casa del Dr Strange fue cambiada a", {nueva_casa})
else:
    print(f"No se encontró a Dr Stange")

#mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
print("\n")
print("Los superheroes que tienen traje o armadura son: ")
for heroe in superHeroes1:
    if heroe["is_villain"] == False:
        biografia = heroe.get("short_bio", "").lower()

        if "suit" in biografia or "armor" in biografia:
            print(f"{heroe["alias"]}")


#mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
#sea anterior a 1963;

print("\n")
print("Nombre y casa de superheroes que aparecieron antes de 1963:")
for heroe in superHeroes1:
    if heroe["is_villain"] == False and heroe["first_appearance"] < 1963:
        print(f"nombre:{heroe["name"]}, casa: {heroe["house"]}")


#mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;

print("\n")
buscado2 = superHeroes1.search("Captain Marvel", "alias")
if buscado2 is not None:
    Capitana_Marvel = superHeroes1[buscado2]
    print(f"La casa de Capitana Marvel es:", {Capitana_Marvel["house"]})
else:
    print(f"No se encontro a Capitana Marvel")

print("\n")
buscado3 = superHeroes1.search("Mujer Maravilla", "alias")
if buscado3 is not None:
    Mujer_Maravilla = superHeroes1[buscado3]
    print(f"La casa de Mujer Maravilla es:", {Mujer_Maravilla["house"]})
else:
    print(f"No se encontro a Mujer Maravilla")


#mostrar toda la información de Flash y Star-Lord;
print("\n")
infoSuperHeroes = List()

buscado4 = superHeroes1.search("Flash", "alias")
if buscado4 is not None:
    infoSuperHeroes =List([superHeroes1[buscado4]])

infoSuperHeroes.show()

buscado5 = superHeroes1.search("Star-Lord", "alias")
if buscado5 is not None:
    infoSuperHeroes = List([superHeroes1[buscado5]])


infoSuperHeroes.show()


#listar los superhéroes que comienzan con la letra B, M y S;

print("\n")
print("Los super heroes cuyos nombres empiezan con B, M, y S, son:  ")
letras = ("B", "M","S")
for heroe in superheroes:
    if heroe["is_villain"] == False:    
        if heroe["alias"].startswith(letras):
            print(f"{heroe["alias"]}")


#determinar cuántos superhéroes hay de cada casa de comic.
ContMarvel = 0
ContDarkHorse = 0
ContDcComics = 0

for heroe in superHeroes1:
    if heroe["house"] == "Marvel":
        ContMarvel += 1
    elif heroe["house"] == "Dark Horse":
        ContDarkHorse += 1
    else:
        ContDcComics += 1

print(f"Los superheroes de la casa Marvel son:{ContMarvel}")
print(f"Los superheroes de la casa Dark Horse son: {ContDarkHorse}")
print(f"Los superheroes de la casa DC Comics son: {ContDcComics}")





jedi = List()

for jed in jedis:
    jedi.append(jed)
    
    
def order_by_name(item):
    return item["nombre"]

def  order_by_especie(item):
    return item["especie"]

def order_by_maestro(item):
    return item("maestro")

jedi.add_criterion("nombre", order_by_name)
jedi.add_criterion("especie", order_by_especie)
jedi.add_criterion("maestros", order_by_maestro)
    
print("-----------------order-by-name---------------------")
jedi.sort_by_criterion("nombre")
jedi.show()
print("-----------------order-by-especie---------------------")
jedi.sort_by_criterion("especie")
jedi.show()

buscadoUno=jedi.search("Ahsoka Tano", "nombre")

if(buscadoUno is not None):
    print(jedi[buscadoUno])
else: print("No fue encontrado")

buscadoDos=jedi.search("Kit Fisto", "nombre")
print(" ")
if(buscadoDos is not None):
    print(jedi[buscadoDos])
else: print("No fue encontrado")


#!mostrar todos los padawan de Yoda y Luke Skywalker
#! , es decir sus aprendices;

for jed in jedi:
    if ("Yoda" in jed["maestros"] or "Luke Skywalker" in jed["maestros"]):
        print(jed)
        print("")
        
#!mostrar los Jedi de especie humana y twi'lek;
for jed in jedi:
    if ("Humano" in jed["especie"] or "Twi'lek" in jed["especie"]):
        print(jed)
        print(" ")
        
#!listar todos los Jedi que comienzan con A;
for jed in jedi:
    if (jed["nombre"].startswith("A")):
        print(jed)
        print("")
        
#!mostrar los Jedi que usaron sable de luz de más de un color;

for jed in jedi:
    if(len(jed["sables_luz"])> 1):
        print(jed)
        print(" ")
        
#!indicar los Jedi que utilizaron sable de luz amarillo o violeta;
for jed in jedi:
    if("Amarillo" in jed["sables_luz"] or "Violeta" in jed["sables_luz"]):
        print(jed)
        print("")

#!indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

for jed in jedi:
    if("Qui-Gon Jinn" in jed["maestros"] or "Mace Windu" in jed["maestros"]):
        print(jed["nombre"])
        print("")
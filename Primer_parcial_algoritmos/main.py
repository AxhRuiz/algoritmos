from Queue import Queue
from List import List
from super_heroes_data import superheroes
def ejercicioUno():
    '''Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
    funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
    funcion recursiva para listar los superheroes de la lista.'''

    superHeroes= ["Superman","Batman", "Spider Man", "Wonder Woman", "Iron Man", "Capitan America", "Thor", "Hulk", "Black Panther", "Flash",
                "Aquaman", "Wolverine", "Black Widow", "Vinterna Verde","Doctor Strange"]

    def searchSuper(arr: list ,buscado : str, i: int=0)-> str:
        
        if i>= len(arr):
            return (f'No se encontraron coincidencias con: {buscado}')
        elif arr[i].lower() == buscado.lower():
            return (f'{buscado} Se encuentra en la lista')
        return searchSuper(arr, buscado, i+1)

    buscar= "Capitan America"

    resultadoBusqueda= searchSuper(superHeroes, buscar)
    print("*****************************************")
    print(resultadoBusqueda)
    print("\n*****************************************")

    def showSuper(arr: list,i: int=0):
        
        if i >= len(arr):
            return
        print(f'* {arr[i]}')
        showSuper(arr, i+1)
        
        

    showSuper(superHeroes)
#ejercicioUno()
def ejercicioDos():

    '''Ejercicio 2: Dada una lista de personajes de marvel (la desarrollada en clases) debe tener 100 o mas, resolver:



    '''
    listSuper= List()
    colaVillanos= Queue()

    def order_by_name(item):
        return item["name"]
    def order_by_realName(item):
        return item["real_name"]
    def order_by_appearance(item):
        return item["first_appearance"]
    def order_by_alias(item):
        return item["alias"]
    def order_by_villain(item):
        return item["is_villain"]

    for superheroe in superheroes:
        listSuper.append(superheroe)
        
    listSuper.add_criterion("name", order_by_name)
    listSuper.add_criterion("real_name", order_by_realName)
    listSuper.add_criterion("first_appearance", order_by_appearance)
    listSuper.add_criterion("alias", order_by_alias)
    listSuper.add_criterion("is_villain", order_by_villain)

    #-Listado ordenado de manera ascendente por nombre de los personajes.
    listSuper.sort_by_criterion("name")
    listSuper.show()
    #-Listado de superheroes ordenados por fecha de aparación.
    '''listSuper.sort_by_criterion("first_appearance")
    listSuper.show()
    '''

    #Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
    '''listSuper.sort_by_criterion("real_name")
    listSuper.show()'''

    # -Determinar en que posicion esta The Thing y Rocket Raccoon.
    '''listSuper.sort_by_criterion("alias")
    pTheThing= listSuper.search("The Thing", "alias")
    pRocket= listSuper.search("Rocket Raccoon", "alias")

    if pTheThing is not None:
        print(f"The Thing se encuentra en la lista y su posicion es: {pTheThing}")
    else:
        print("The Thing no se encuentra en la lista")
    if pRocket is not None:
        print(f"The Thing se encuentra en la lista y su posicion es: {pRocket}")
    else:
        print("The Thing no se encuentra en la lista")'''

    #-Listar todos los villanos de la lista.  
    '''listSuper.sort_by_criterion("is_villain")
    listSuper.reverse()

    for villano in listSuper:
        if villano["is_villain"]:
            print(villano)'''
            
    #-Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
    '''
    for villano in listSuper:
        if (villano["first_appearance"] <1980) and villano["is_villain"]:
            colaVillanos.arrive(villano)
    #colaVillanos.show()'''

    #-Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
    """for sup in listSuper:
        if (("time-traveling") in sup["short_bio"].lower()) or ("suit" in sup["short_bio"].lower()):
            print(sup)
    """
    #-Modificar el nombre real de Ant Man a Scott Lang.
    """pAnt=listSuper.search("Ant Man", "name")
    if pAnt:
        listSuper[pAnt]["real_name"]= "Scott Lang"

    print(listSuper[pAnt])"""
    #-Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.
    '''
    pElectro= listSuper.search("Electro","name")
    pBaron= listSuper.search("Baron Zemo", "name")

    if pElectro:
        print(listSuper[pElectro]["short_bio"])
        listSuper.pop(pElectro)
    if pBaron:
        print(listSuper[pBaron]["short_bio"])
        listSuper.pop(pBaron)
    '''

    #-Listar los superheores que comienzan con  Bl, G, My, y W.
    '''
    lt=("Bl", "G", "My", "W")
    for sup in listSuper:
        if sup["name"].startswith(lt):
            print(sup["name"])
    '''

ejercicioDos()



    

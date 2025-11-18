from tree import BinaryTree
from random import shuffle
from pokemonsData import pokemons_data

# Datos de ejemplo de Pokémons (simularemos algunos para demostrar)
# En el examen real tendrías los 1025 pokémons


# Mezclar datos aleatoriamente como indica el ejercicio
shuffle(pokemons_data)

# Crear los tres árboles
arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()


# Cargar datos en los árboles
for pokemon in pokemons_data:
    # Preparar other_values sin el índice correspondiente
    
    # Árbol por nombre
    info_nombre = {
        'numero': pokemon['numero'],
        'tipos': pokemon['tipos'],
        'debilidades': pokemon['debilidades'],
        'megaevolucion': pokemon['megaevolucion'],
        'gigamax': pokemon['gigamax']
    }
    arbol_nombre.insert(pokemon['nombre'], info_nombre)
    
    # Árbol por número
    info_numero = {
        'nombre': pokemon['nombre'],
        'tipos': pokemon['tipos'],
        'debilidades': pokemon['debilidades'],
        'megaevolucion': pokemon['megaevolucion'],
        'gigamax': pokemon['gigamax']
    }
    arbol_numero.insert(pokemon['numero'], info_numero)
    
    # Árbol por tipo - para cada tipo del pokémon
    for tipo in pokemon['tipos']:
        info_tipo = {
            'nombre': pokemon['nombre'],
            'numero': pokemon['numero'],
            'tipos': pokemon['tipos'],
            'debilidades': pokemon['debilidades'],
            'megaevolucion': pokemon['megaevolucion'],
            'gigamax': pokemon['gigamax']
        }
        arbol_tipo.insert(tipo, info_tipo)




print("1. BÚSQUEDA POR NÚMERO")
numero_buscar = 9
pos = arbol_numero.search(numero_buscar)
if pos is not None:
    print(f"Pokémon {numero_buscar}:")
    print(f"Nombre: {pos.other_values['nombre']}")
    print(f"Tipos: {', '.join(pos.other_values['tipos'])}")
    print(f"Debilidades: {', '.join(pos.other_values['debilidades'])}")
    print(f"Megaevolución: {'Sí' if pos.other_values['megaevolucion'] else 'No'}")
    print(f"Gigamax: {'Sí' if pos.other_values['gigamax'] else 'No'}")
else:
    print(f"No se encontró el Pokémon #{numero_buscar}")
print()


print("2. BÚSQUEDA POR NOMBRE (PROXIMIDAD)")
print("Buscando Pokémons que contengan 'Char':")
arbol_nombre.proximity_search('Char')
print()


print("3. POKÉMONS POR TIPO")

def mostrar_por_tipo(arbol, tipo_buscar):
    
    def __buscar_tipo(root, tipo_buscar):
        if root is not None:
            __buscar_tipo(root.left, tipo_buscar)
            if root.value == tipo_buscar:
                print(f"{root.other_values['nombre']} ")
            __buscar_tipo(root.right, tipo_buscar)
    
    print(f"\nPokémons tipo {tipo_buscar.upper()}:")
    if arbol.root is not None:
        __buscar_tipo(arbol.root, tipo_buscar)


for tipo in ["fantasma", "fuego", "acero", "electrico"]:
    mostrar_por_tipo(arbol_tipo, tipo)

print()


print("4. LISTADOS ORDENADOS")

print("\nListado por número (in-order):")
def in_order_numero(arbol):
    def __in_order(root):
        if root is not None:
            __in_order(root.left)
            print(f"  {root.value}. {root.other_values['nombre']}")
            __in_order(root.right)
    
    if arbol.root is not None:
        __in_order(arbol.root)

in_order_numero(arbol_numero)

print("\nListado por nombre (in-order):")
arbol_nombre.in_order()

print("\nListado por nombre (por nivel):")
arbol_nombre.by_level()
print()


print("5. POKÉMONS DÉBILES FRENTE A JOLTEON, LYCANROC Y TYRANTRUM")


jolteon = arbol_numero.search(135)
lycanroc = arbol_numero.search(745)
tyrantrum = arbol_numero.search(697)

tipos_atacantes = []
if jolteon is not None:
    tipos_atacantes.extend(jolteon.other_values['tipos'])
if lycanroc is not None:
    tipos_atacantes.extend(lycanroc.other_values['tipos'])
if tyrantrum is not None:
    tipos_atacantes.extend(tyrantrum.other_values['tipos'])

print(f"Tipos de ataque: {', '.join(set(tipos_atacantes))}")
print("\nPokémons débiles:")

def mostrar_debiles(arbol, tipos_ataque):
    def __mostrar_debiles(root, tipos_ataque):
        if root is not None:
            __mostrar_debiles(root.left, tipos_ataque)
            # Verificar si tiene alguna debilidad contra los tipos
            debilidades = root.other_values['debilidades']
            tipos_comunes = set(debilidades) & set(tipos_ataque)
            if tipos_comunes:
                print(f"{root.other_values['nombre']} es débil a: {', '.join(tipos_comunes)}")
            __mostrar_debiles(root.right, tipos_ataque)
    
    if arbol.root is not None:
        __mostrar_debiles(arbol.root, tipos_ataque)

mostrar_debiles(arbol_numero, tipos_atacantes)
print()


print("6. TIPOS DE POKÉMONS Y CANTIDAD")

def contar_tipos(arbol):
    
    conteo = {}
    
    def __contar(root):
        if root is not None:
            __contar(root.left)
            tipo = root.value
            if tipo not in conteo:
                conteo[tipo] = 0
            conteo[tipo] += 1
            __contar(root.right)
    
    if arbol.root is not None:
        __contar(arbol.root)
    
    return conteo

tipos_conteo = contar_tipos(arbol_tipo)
print("\nCantidad de Pokémons por tipo:")
for tipo, cantidad in sorted(tipos_conteo.items()):
    print(f"{tipo.capitalize()}: {cantidad}")
print()


print("7. POKÉMONS CON MEGAEVOLUCIÓN")

def contar_megaevolucion(arbol):
    def __contar(root):
        count = 0
        if root is not None:
            if root.other_values['megaevolucion'] is True:
                count += 1
            count += __contar(root.left)
            count += __contar(root.right)
        return count
    
    total = 0
    if arbol.root is not None:
        total = __contar(arbol.root)
    return total

total_mega = contar_megaevolucion(arbol_numero)
print(f"Total de Pokémons con megaevolución: {total_mega}")
print()


print("8. POKÉMONS CON FORMA GIGAMAX")

def contar_gigamax(arbol):
    def __contar(root):
        count = 0
        if root is not None:
            if root.other_values['gigamax'] is True:
                count += 1
            count += __contar(root.left)
            count += __contar(root.right)
        return count
    
    total = 0
    if arbol.root is not None:
        total = __contar(arbol.root)
    return total

total_gigamax = contar_gigamax(arbol_numero)
print(f"Total de Pokémons con forma Gigamax: {total_gigamax}")
print()


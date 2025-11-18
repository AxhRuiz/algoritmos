from graph import Graph

grafo_star_wars = Graph(is_directed=True)

print("=== CARGANDO PERSONAJES DE STAR WARS ===\n")
personajes_data = [
    {'nombre': 'Luke Skywalker', 'episodios': [4, 5, 6, 7, 8, 9]},
    {'nombre': 'Darth Vader', 'episodios': [3, 4, 5, 6]},
    {'nombre': 'Yoda', 'episodios': [1, 2, 3, 5, 6, 8, 9]},
    {'nombre': 'Boba Fett', 'episodios': [5, 6]},
    {'nombre': 'C-3PO', 'episodios': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    {'nombre': 'Leia', 'episodios': [3, 4, 5, 6, 7, 8, 9]},
    {'nombre': 'Rey', 'episodios': [7, 8, 9]},
    {'nombre': 'Kylo Ren', 'episodios': [7, 8, 9]},
    {'nombre': 'Chewbacca', 'episodios': [3, 4, 5, 6, 7, 8, 9]},
    {'nombre': 'Han Solo', 'episodios': [4, 5, 6, 7]},
    {'nombre': 'R2-D2', 'episodios': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    {'nombre': 'BB-8', 'episodios': [7, 8, 9]},
]

for personaje in personajes_data:
    grafo_star_wars.insert_vertex(personaje['nombre'])
    pos = grafo_star_wars.search(personaje['nombre'], 'value')
    if pos is not None:
        grafo_star_wars[pos].other_values = {'episodios': personaje['episodios']}

relaciones = [
    ('Luke Skywalker', 'Leia', 5),
    ('Luke Skywalker', 'Han Solo', 3),
    ('Luke Skywalker', 'Chewbacca', 4),
    ('Luke Skywalker', 'C-3PO', 6),
    ('Luke Skywalker', 'R2-D2', 6),
    ('Luke Skywalker', 'Darth Vader', 3),
    ('Luke Skywalker', 'Yoda', 3),
    ('Leia', 'Han Solo', 5),
    ('Leia', 'Chewbacca', 7),
    ('Leia', 'C-3PO', 7),
    ('Leia', 'R2-D2', 7),
    ('Han Solo', 'Chewbacca', 5),
    ('Han Solo', 'C-3PO', 4),
    ('Han Solo', 'R2-D2', 4),
    ('Chewbacca', 'C-3PO', 7),
    ('Chewbacca', 'R2-D2', 7),
    ('C-3PO', 'R2-D2', 9),
    ('Darth Vader', 'Boba Fett', 2),
    ('Yoda', 'R2-D2', 4),
    ('Yoda', 'C-3PO', 4),
    ('Rey', 'Kylo Ren', 3),
    ('Rey', 'BB-8', 3),
    ('Rey', 'Leia', 3),
    ('Rey', 'Chewbacca', 3),
    ('Rey', 'C-3PO', 3),
    ('Rey', 'R2-D2', 3),
    ('Kylo Ren', 'Leia', 2),
    ('Kylo Ren', 'Han Solo', 1),
    ('BB-8', 'Leia', 2),
    ('BB-8', 'C-3PO', 2),
    ('BB-8', 'R2-D2', 2),
    ('BB-8', 'Chewbacca', 3),
    ('Yoda', 'Chewbacca', 2),
    ('Boba Fett', 'Han Solo', 1),
    ('Darth Vader', 'C-3PO', 3),
    ('Darth Vader', 'R2-D2', 3),
    ('Darth Vader', 'Leia', 3),
    ('Darth Vader', 'Chewbacca', 2),
]

for origen, destino, episodios in relaciones:
    grafo_star_wars.insert_edge(origen, destino, episodios)

print("1. ÁRBOL DE EXPANSIÓN MÍNIMO (KRUSKAL)")

personajes_inicio = ['C-3PO', 'Yoda', 'Leia']

for personaje in personajes_inicio:
    print(f"Árbol de expansión mínimo desde {personaje}")
    expansion_tree = grafo_star_wars.kruskal(personaje)
    
    if isinstance(expansion_tree, str):
        print(f"Árbol: {expansion_tree}\n")
        peso_total = 0
        print("Conexiones del árbol:")
        for edge in expansion_tree.split(';'):
            partes = edge.split('-')
            if len(partes) == 3:
                origen, destino, weight = partes
                print(f"  {origen} y {destino}: {weight} episodios")
                peso_total += int(weight)
        print(f"\nPeso total del árbol: {peso_total}")
    else:
        print(f"Árbol: {expansion_tree}")

print("\n2. MÁXIMO DE EPISODIOS COMPARTIDOS")

max_episodios = 0
parejas_max = []

for vertex in grafo_star_wars:
    for edge in vertex.edges:
        if edge.weight > max_episodios:
            max_episodios = edge.weight
            parejas_max = [(vertex.value, edge.value)]
        elif edge.weight == max_episodios:
            pareja_ordenada = tuple(sorted([vertex.value, edge.value]))
            parejas_ordenadas_existentes = [tuple(sorted(p)) for p in parejas_max]
            if pareja_ordenada not in parejas_ordenadas_existentes:
                parejas_max.append((vertex.value, edge.value))

print(f"Número máximo de episodios compartidos: {max_episodios}")
print(f"Parejas que comparten {max_episodios} episodios juntos:")
for pareja in parejas_max:
    print(f"{pareja[0]} y {pareja[1]}")

print("\n4. CAMINO MÁS CORTO (DIJKSTRA)")

def obtener_camino_dijkstra(grafo, origen, destino):
    path = grafo.dijkstra(origen)
    peso_total = None
    camino_completo = []
    destino_actual = destino
    
    while path.size() > 0:
        value = path.pop()
        if value[0] == destino_actual:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destino_actual = value[2]
    
    camino_completo.reverse()
    return camino_completo, peso_total

print("\nCamino más corto: C-3PO a R2-D2")
camino, costo = obtener_camino_dijkstra(grafo_star_wars, 'C-3PO', 'R2-D2')

if len(camino) > 0:
    print(f"Camino: {''.join(camino)}")
    print(f"Costo total:{costo}")
else:
    print("No existe camino entre C-3PO y R2-D2")

print("\nCamino más corto: Yoda a Darth Vader")
camino, costo = obtener_camino_dijkstra(grafo_star_wars, 'Yoda', 'Darth Vader')

if len(camino) > 0:
    print(f"Camino: {''.join(camino)}")
    print(f"Costo total:{costo}")
else:
    print("No existe camino entre Yoda y Darth Vader")

print("\n5. PERSONAJES EN LOS 9 EPISODIOS")


personajes_9_episodios = []

for vertex in grafo_star_wars:
    if vertex.other_values and 'episodios' in vertex.other_values:
        if len(vertex.other_values['episodios']) == 9:
            personajes_9_episodios.append(vertex.value)

print(f"Personajes que aparecieron en los 9 episodios de la saga:")
if personajes_9_episodios:
    for personaje in personajes_9_episodios:
        pos = grafo_star_wars.search(personaje, 'value')
        if pos is not None:
            episodios = grafo_star_wars[pos].other_values['episodios']
            print(f"{personaje}")
            print(f"Episodios: {episodios}")
    print(f"\nTotal: {len(personajes_9_episodios)} personaje(s)")
else:
    print("No hay personajes que aparezcan en los 9 episodios")



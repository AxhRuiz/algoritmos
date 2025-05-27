

from pprint import pprint
from collections import deque

def notificaciones(hora, app, mensaje):
    return {
        "hora": hora,
        "app": app,
        "mensaje": mensaje
    }


cola_notificaciones = deque ([
{"hora": "11:47","app": "facebook","mensaje": "Hola, como estas?"},
{"hora":"12:30","app": "instagram","mensaje":  "Que haces"},
{"hora":"12:45","app": "instagram","mensaje":  "Que comemos?"},
{"hora":"11:58","app": "telegram", "mensaje": "A cuanto?"},
{"hora":"15:12","app": "facebook", "mensaje": "No voy a ir"},
{"hora":"16:45","app": "facebook", "mensaje": "Compra una fresca"},  
{"hora":"18:25","app": "telegram", "mensaje": "Ahora paso"},
{"hora":"19:45","app": "instagram","mensaje":  "Hoy te vi!"},
{"hora":"20:20","app": "facebook", "mensaje": "Y.. Axel es terrible"},
{"hora":"01:15","app": "Instagram","mensaje":  "Estas para House?"},
{"hora":"17:14","app": "twitter",  "mensaje": "sabes phyton?"},
{"hora":"11:59","app": "twiter",   "mensaje": "Mañana paso por ahí"},
{"hora":"12:01","app": "twitter",  "mensaje": "tenes lo de phyton?"},

])

print("ITEM A")
print("\nTodas las notificaciones:")
pprint(cola_notificaciones)

cola_para_itemA = deque(cola_notificaciones.copy())
notificaciones_sin_facebook = deque()

while cola_para_itemA:
    notificacion = cola_para_itemA.popleft()
    if notificacion["app"] != "facebook":
        notificaciones_sin_facebook.append(notificacion)


print("\nCola modificada sin notificaciones de facebook")
pprint(notificaciones_sin_facebook)




print("\n")
print("ITEM B")

cola_para_itemB = deque(cola_notificaciones.copy())
mostrar_notif_twitter = deque()

while cola_para_itemB:
    notificacion = cola_para_itemB.popleft()
    if (notificacion["app"].lower() == "twitter" and "phyton" in notificacion["mensaje"].lower()):
        mostrar_notif_twitter.append(notificacion)

print("Las notificiaciones de twitter que contienen la palabra phyton son: ")
pprint(mostrar_notif_twitter)


print("\n")
print("ITEM C")


cola_para_itemC = deque(cola_notificaciones.copy())
pila_rango_horario = deque()

for i in cola_para_itemC:
    if i["hora"] > "11:43" and i["hora"] < "15:57":
        pila_rango_horario.append(i)

print("Las notificaciones que llegaron entre las 11:43 y las 15:57 son: ")
pprint(pila_rango_horario)


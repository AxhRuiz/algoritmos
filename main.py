# ROMANO A DECIMAL #

import romano_a_decimal

number = input("Ingrese un numero romano: ")
print(f"El numero en decimal es: {romano_a_decimal.romano_a_decimal(number)}")

# LA MOCHILA DEL JEDI #

import usar_la_fuerza

#defino la mochila con los siguientes objetos:
mochila = ["comida", "botiquín", "cuerda", "sable de luz", "agua"]

encontrado, cantidad = usar_la_fuerza.usar_la_fuerza(mochila)

if encontrado:
    print(f"Sable encontrado, Se sacaron {cantidad} objetos.")
else:
    print("No se encontró el sable de luz.")
    
# FINAL DEL CODIGO #
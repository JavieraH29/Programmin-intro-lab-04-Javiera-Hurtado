# Similar a los arreglos, los diccionarios nos permiten
# estructurar información, Con la diferencia de que los 
# elementos están ordenados por llave y no por índice. Ejemplo

my_car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year" : 2022,
    "options" : ["5 puertas", "Aire acondicioado", "Frenos ABS"],
    "available": True
}

print(my_car["brand"])
print(my_car["year"])
print(my_car["options"])

#Si queremos todas las llaves tenemos el método .keys()
print(my_car.keys())
# Si queremos todos los valores, tnemos el método values()
print(my_car.values())

# Podemos también actualizar valores de una determinada llave

my_car["model"] = "Raize"

print(my_car["model"])

# También podemos agregar llaves y valores
my_car["color"] = "grey"
print(my_car)

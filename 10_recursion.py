import time
# Es perfectamente posible llamar un función dentro de otra. Los hicimos cuando calculamos el volumen de un cilindro
# Pero también es perfectamente posible que una función se llame a si misma.
# Esta es una técnica muy poderosa para ciertos problemas.

# Función conteo regresivo 
# Función que se llama a si misma
def countdown(number):
    if number <= 0:
        print("KABUUUM")
    else: 
        print(number)
        time.sleep(0.5)
        countdown(number - 1)

countdown(5)

def super_sum (number):
    if number <= 0:
        return number
    else:
        return number + super_sum(number -1)

print (super_sum(10))

# Otra forma es crear una lista con un rango de caracteres para luego hacer iterar la lista. Es este caso de 1 a 10, se escribe 11 porque el rango va de 1 a 11, era no incluye el 11

total = 0 
for list_elem in range(1,11):
    total = total + list_elem

print(total)

#Recursión infinita, sin condición de salida. Para nada util, pero entretenida.
def infinite():
    infinite()

infinite()
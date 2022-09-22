# Tenemos expresiones que se pueden evaluar en terminos booleanos o dicotomicos
# Ejemplo

print(10 > 9)

# Esto nos permita hacer ejecuciones condicionales, por ejemplo

def is_adult(age):
    if age >= 18:
        return True
    else: 
        return False

# Estas siguentes instrucciones las podríamos leer como: "si(if el resultado de is_adult ejecutada con la variación Gby_age es verdadero, entonces el programa imprime "Quieres una cerveza?. De todo modo (else), imprime "cantemos chuchuwa?""

gaby_age = 45
paola_age =30

if is_adult(gaby_age):
    print("Quieres una cerveza")
else:
    print("Cantemos chuchuwa")

if is_adult(paola_age):
    print("¿Quieres una cerveza?")
else:
    print("Cantemos chuchuwa")

if gaby_age > paola_age:
    diff = paola_age - gaby_age
    if diff < 5:
        print("Paola es menor que gaby por menos de 5 años")
    elif diff < 10:
        print("Paola es menor que Gaby por menos de 10")
    else:
        print("Paola es mayor que Gaby por mas de 10")
    #print("Gaby es mayor que Paola")
elif gaby_age == paola_age:
    print("Paola y Gaby tienen la  misma edad")
elif gaby_age > paola_age + 10:
    print("Gaby es mayor que Paola por 11 o mas años")
else:
    print("Paola es mayor que Gaby")
    
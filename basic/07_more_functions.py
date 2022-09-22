# Podemos crear o definir nuestras propias funciones
# Lo hacemos con la palabra especial "def" y el cuerpo 
# La función debe ir correctamente identada
import time

def chuchuwa(inst):
    print("Chuchuwa chuchuwa chuchuwa wa wa")
    time.sleep(3.5)
    print("Chuchuwa chuchuwa chuchuwa wa wa")
    time.sleep(3.5)
    print("Atención")
    time.sleep(1.5)
    print("Compañia")
    time.sleep(1.5)
    print(inst)
    time.sleep(1.)
    print("Y!!!")

print(Chuchuwa)
print(tpe(Chuchuwa))

# Las funciones son otro tipo de variables

# El llamado de la función

chuchuwa("Mano hacia el frente")
time.sleep(2)
chuchuwa("Hombro hacia atras")
time.sleep(2)
chuchuwa("Lengua afuera")
time.sleep(2)

result=chuchuwa("Lengua afuera")

# Si la función no tiene un valor de retorno, la variable definida como result, nos entregara none, que es para representar nada
print(results)

# En función chuchuwa(inst) el argumento 'inst' es un parámetro requerido y por lo tanto no puede lanzarse la función sin tener un parámetro
# Para hacer programas interativos y obtener datos del usuario tenemos la función inpu(), que recibe como argumento lo que pedira la consola
a1 = 'Nunca lo sabrasa...'
name = input('Hola, como te llamas\n')
print('Hola', name, 'gusto en conocerte, conozcamos tu IMC')
'''q1 = input('¿Quieres conocer tu IMC? (Y/N)\n')'''
'''if q1 == 'Y':
    return weight
else:
    print(a1)'''
weight = int(input('Ingresa tu peso en Kg: \n'))
weight = int(input('Ahora dime tu altura en centimetros: \n'))
 
 IMC = weight * height ** 2 

 if IMC in range(18.5,24.99)
    print(name, '¡¡¡', 'Estas en tu peso!!!')
elif IMC =< 18.5:
    print(name, 'Cuidado, te encuentras bajo peso, consulta con un profesional de la nutrición')
elif IMC in range(25,29.99):
    print(name, 'Estas ligeramente sobrepeso, pero tranquilo, es solo un poco')
elif IMC in range(30, 34.99)
    print(name, 'Cuidado, tienes obesidad grado 1')
elif IMC > 40 
    print(name, 'Mucho cuidado, tienes obesidad morbida. Asesorate con un profesional de la nutrición')
else:
    print('No result')
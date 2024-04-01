#Condicionales 
#1
"""
par = float(input('Ingrese un numero par: '))
impar = float(input('Ingrese un numero impar: '))

if par % 2 != 0 or impar % 2 == 0:
    print('Uno de los valores es incorrecto.')"""

#2 
"""
par = float(input('Ingrese un numero par: '))

if par % 2 == 0:
    impar = float(input('Ingrese un numero impar: '))

    if impar % 2 == 0:
        print('Valor incorrecto.')

else:
    print('Valor incorrecto.')

"""

#3
"""
par = float(input('Ingrese un numero par: '))
impar = float(input('Ingrese un numero impar: '))

if par % 2 != 0:
    print('Valor par incorrecto.')

if impar % 2 == 0:
    print('Valor impar incorrecto.')"""

#5
"""
num_uno = int(input('Ingrese el primer valor: '))
num_dos = int(input('Ingrese el segundo valor: '))

if num_uno % num_dos == 0:
    print('Division exacta.')
else:
    print('Division inexacta.')
"""

#6
"""
num_uno = int(input('Ingrese el primer valor: '))
num_dos = int(input('Ingrese el segundo valor: '))

if num_dos != 0:
    if num_uno % num_dos == 0:
        print('Division exacta.')
    else:
        print('Division inexacta.')
else:
    print('Division no valida.')"""

#8
"""
cualquiera = int(input('Ingrese anho cualquiera: '))
actual = int(input('Ingrese anho actual: '))

if actual > cualquiera:
    pasado = actual - cualquiera
    print('Ese anho fue hace ' + str(pasado))

elif actual < cualquiera:
    futuro = cualquiera - actual
    print('Faltan ' + str(futuro) + ' anhos.')

#esto se agrega en el siguiente
else:
    print('Estamos en ese anho.')"""





correo = 'josiascaceresvillalba@gmail.com'

#para extraer nombre
arroba = correo.find('@')

nombre_usuario = correo[0: arroba]

print(nombre_usuario)

#para extraer el dominio
punto = correo.find('.')

dominio = correo[arroba + 1:punto]

print(dominio)



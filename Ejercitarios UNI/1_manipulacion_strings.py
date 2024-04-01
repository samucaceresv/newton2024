#1
"""
nombre_usuario = "Josias"
numero_entero = 2
print(nombre_usuario * numero_entero)"""
#2 
"""
nombre_usuario = "Josias"
apellido_usuario = "Caceres"

nombre_completo = nombre_usuario + " " + apellido_usuario

numero_entero = 10

print((nombre_completo + '\n') * numero_entero)"""

#3
"""
nombre = 'Josias'
apellido = 'Caceres'

nombre_completo = nombre + ' ' + apellido

n = len(nombre_completo.replace(' ', ''))

print(nombre_completo + ' tiene ' + str(n) + ' letras.')
"""

#4
"""
producto = input('Ingrese el nombre del producto: ')
precio_unitario = int(input('Ingrese el precio unitario del producto: '))
cantidad = int(input('Ingrese la cantidad de unidades: '))

precio_total = precio_unitario * cantidad

cantidad_str = str(cantidad)
precio_unitario_str = str(precio_unitario)
precio_total_str = str(precio_total)

longitud_precio_unitario_str = len(precio_unitario_str)
longitud_cantidad_str = len(cantidad_str)
longitud_precio_total_str = len(precio_total_str)

precio_unitario_final = ('0' * (6 - longitud_precio_unitario_str)) + precio_unitario_str
cantidad_final = ('0' * (3 - longitud_cantidad_str)) + cantidad_str
precio_total_final = ('0' * (8 - longitud_precio_total_str)) + precio_total_str

print(producto + '_' + precio_unitario_final + '_' + cantidad_final + '_' + precio_total_final)
"""

#5
"""
frase = 'hola a todos'
vocal = 'a' 
frase += vocal.upper()

print(frase)"""

#6
"""
texto = 'Hola Mundo'
n = 5

print((texto + ' ') * n)"""

#7
"""libro_nombre = 'Harry Potter'
cantidad_letras = len(libro_nombre.replace(' ', ''))
print('El libro ' + libro_nombre + ' tiene ' + str(cantidad_letras) + 'caracteres.')"""
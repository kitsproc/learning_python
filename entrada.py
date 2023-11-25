#Entrada de datos desde el teclado

nombre = input("Ingresa tu nombre completo: ")
print(type(nombre))
print(nombre)

edad = input("Ingresa su edad: ")
edad = int(edad)#Genera un numero entero
print(type(edad))
print(edad)

altura = float(input("Ingresa tu altura: "))
print(type(altura))
print(altura)

autorizacion = bool(input("Autorizas el programa? (si/no) "))
respuesta = autorizacion=="si"
print(type(respuesta))
print(respuesta)
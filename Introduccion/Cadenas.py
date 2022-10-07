#Cadenas de texto

texto="Programación de MediaNoche"

print("TEXTO COMPLETO")
print(texto)

print(" ")
print("IMPRIME LA PRIMERA LETRA")
print(texto[0])

print(" ")
print("IMPRIME LA PALABRA DEL MEDIO")
print(texto[13:15])

print(" ")
print("IMPRIME LA ULTIMA PALABRA")
print(texto[-10:])

#Funciones con Cadenas

print(" ")
print("IMPRIME LA PALABRA EN MAYUSCULAS")
print(texto[13:15].upper())

print(" ")
print("TEXTO COMPLETO EN MINUSCULAS")
print(texto.lower())

print(" ")
print("IMPRIME LA PALABRA CON INICIAL MAYUSCULA")
print(texto[13:15].capitalize())

#Elementos separados por coma
cadena="html,css,sass,less,javascript,angular"

print(" ")
print("IMPRIME CADENA COMPLETA")
print(cadena)

print(" ")
print("CADENA COMO ARREGLO")
print(cadena.split(','))
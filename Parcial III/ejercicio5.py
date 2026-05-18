# Ejercicio 5: Transformación de nombre con privacidad

# Solicita el nombre completo del usuario
nombre_completo = input("Ingrese su nombre completo (Nombre y Apellido): ")

# Convierte el texto en lista y la invierte con slicing negativo
lista_nombre = nombre_completo.split()[::-1]

# Implementa bucles anidados para formatear las letras
for palabra in lista_nombre:          # Primer bucle: recorre las palabras (apellido, nombre)
    for letra in palabra:             # Segundo bucle: recorre cada letra
        print(letra, end=".")         # Imprime cada letra separada por punto
    print()                           # Salto de línea entre apellido y nombre
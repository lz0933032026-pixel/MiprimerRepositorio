# Ejercicio 1: Slicing y Ternario

# Solicita al usuario una etiqueta de rastreo
codigo = input("Ingrese el código de rastreo (AÑO-CATEGORÍA-PAÍS): ")

# Validación de seguridad
if not codigo:  # Si está vacío o None
    print("Error: el código no puede estar vacío.")
else:
    # Extrae la categoría usando slicing
    partes = codigo.split("-")
    categoria = partes[1]  # sección central
    print("Categoría:", categoria)

    # Aplica el operador ternario para definir la ruta
    ruta = "Ruta Local" if codigo.endswith("SV") else "Ruta Internacional"
    print(ruta) 
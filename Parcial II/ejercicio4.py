# 1. Crear la variable con la palabra
palabra = "CANTANDO"

# 2. Convertir toda la cadena a letras minúsculas
palabra_minuscula = palabra.lower()

# 3. Eliminar el sufijo "ando" y encontrar el índice de la letra "t"
palabra_sin_sufijo = palabra_minuscula.removesuffix("ando")
indice_t = palabra_sin_sufijo.find("t")

# Mostrar resultados
print("Palabra en minúsculas:", palabra_minuscula)
print("Palabra sin sufijo:", palabra_sin_sufijo)
print("Índice de la letra 't':", indice_t)
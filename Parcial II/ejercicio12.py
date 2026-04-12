# 1. Tomar el nombre de archivo
archivo = "Sunombre.txt"

# 2. Remover el sufijo ".txt" y posteriormente el prefijo "ING. "
archivo_sin_sufijo = archivo.removesuffix(".txt")
archivo_sin_prefijo = archivo_sin_sufijo.removeprefix("ING. ")

# 3. Convertir el texto limpio a minúsculas
archivo_final = archivo_sin_prefijo.lower()

# Mostrar resultados
print("Archivo sin sufijo:", archivo_sin_sufijo)
print("Archivo sin prefijo:", archivo_sin_prefijo)
print("Archivo final:", archivo_final)
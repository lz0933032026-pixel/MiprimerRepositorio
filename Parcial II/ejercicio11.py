# 1. Tomar la cadena
texto = "  el nido matinal  "

# 2. Limpiar los espacios en blanco de los extremos y poner la primera letra de cada palabra en mayúscula
texto_limpio = texto.strip().title()

# 3. Centrar el texto en un espacio total de 30 caracteres, rellenando con guiones medios
texto_centrado = texto_limpio.center(30, "-")

# Mostrar resultados
print("Texto limpio:", texto_limpio)
print("Texto centrado:", texto_centrado)
# 1. Crear la variable con el texto
texto = "ING. Su nombre"

# 2. Remover el prefijo "ING. "
texto_sin_prefijo = texto.removeprefix("ING. ")

# 3. Convertir el texto restante completamente a mayúsculas
texto_final = texto_sin_prefijo.upper()

# Mostrar resultados
print("Texto sin prefijo:", texto_sin_prefijo)
print("Texto final:", texto_final)
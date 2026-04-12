# 1. Iniciar con la cadena
texto = "pYTHON"

# 2. Invertir mayúsculas y minúsculas
texto_invertido = texto.swapcase()

# 3. Alinear el texto hacia la izquierda en un espacio de 15 caracteres, rellenando con asteriscos
texto_final = texto_invertido.ljust(15, "*")

# Mostrar resultados
print("Texto invertido:", texto_invertido)
print("Texto final alineado:", texto_final)
# 1. Declarar la cadena de texto
texto = "Su nombre"

# 2. Convertir la primera letra de cada palabra en mayúscula
texto_titulo = texto.title()

# 3. Reemplazar "Su nombre" por "Su apellido"
texto_final = texto_titulo.replace("Su nombre", "Su apellido")

# Mostrar el resultado
print("Texto convertido:", texto_titulo)
print("Texto final:", texto_final) 
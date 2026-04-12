# 1. Tomar el texto
texto = "Su nombre"

# 2. Aplicar el método de normalización fuerte (casefold)
texto_normalizado = texto.casefold()

# 3. Verificar si el texto está compuesto únicamente por letras
solo_letras = texto_normalizado.isalpha()

# Mostrar resultados
print("Texto normalizado:", texto_normalizado)
print("¿Solo letras?:", solo_letras)
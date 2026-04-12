# 1. Tomar la cadena
texto = "Python2026"

# 2. Verificar si el texto es estrictamente alfanumérico
es_alfanumerico = texto.isalnum()

# 3. Si lo es, convertir el texto a minúsculas y reemplazar "2026" por una cadena vacía
if es_alfanumerico:
    texto_modificado = texto.lower().replace("2026", "")
else:
    texto_modificado = "El texto no es alfanumérico"

# Mostrar resultados
print("¿Es alfanumérico?:", es_alfanumerico)
print("Texto modificado:", texto_modificado)
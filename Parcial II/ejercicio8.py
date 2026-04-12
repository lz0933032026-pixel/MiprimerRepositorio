# 1. Definir un bloque de texto de 3 líneas usando comillas triples
poema = """La luna brilla clara
sobre el agua callada
y el alma se prepara"""

# 2. Contar cuántas veces aparece la letra "a" en todo el bloque de texto
conteo_a = poema.count("a")

# 3. Dividir el bloque de texto por sus saltos de línea para convertirlo en una lista
lineas = poema.splitlines()

# Mostrar resultados
print("Bloque de texto:\n", poema)
print("Cantidad de 'a':", conteo_a)
print("Lista de líneas:", lineas)
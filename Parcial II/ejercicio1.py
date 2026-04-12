# 1. Declarar la variable con espacios en los extremos
animal = "  elefante  "

# 2. Limpiar los espacios en blanco de ambos extremos con strip()
animal_limpio = animal.strip()

# 3. Contar cuántas veces aparece la letra "e"
conteo_e = animal_limpio.count("e")

# Mostrar resultados
print("Texto limpio:", animal_limpio)
print("Cantidad de 'e':", conteo_e) 
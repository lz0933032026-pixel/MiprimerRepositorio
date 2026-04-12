# 1. Tomar el texto numérico
numero = "42"

# 2. Rellenar con ceros a la izquierda hasta alcanzar una longitud de 5 caracteres
numero_rellenado = numero.zfill(5)

# 3. Verificar si la nueva cadena termina con el número "2"
termina_en_dos = numero_rellenado.endswith("2")

# Mostrar resultados
print("Número rellenado:", numero_rellenado)
print("¿Termina en '2'?:", termina_en_dos)
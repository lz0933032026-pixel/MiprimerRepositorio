# Ejercicio 4: Auditoría de registros

# Recorre un rango de 1 a 50
for registro in range(1, 51):

    # Filtro de omisión: múltiplos de 3 (registros corruptos)
    if registro % 3 == 0:
        continue  # salta el registro sin imprimir nada

    # Protocolo de parada: amenaza de seguridad
    if registro == 42:
        print("⚠️ Alerta: amenaza de seguridad detectada. Proceso detenido.")
        break  # detiene todo el proceso

    # Caso normal: registro válido
    print(f"Procesando registro ID: {registro}")
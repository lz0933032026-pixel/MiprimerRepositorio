# Ejercicio 3: Lecturas de temperatura y alertas

# Solicita 5 lecturas de temperatura y las guarda en una lista
lecturas = []
for i in range(5):
    valor = int(input(f"Ingrese la lectura de temperatura #{i+1}: "))
    lecturas.append(valor)

# Itera la lista y evalúa cada lectura con match-case
for temp in lecturas:
    match temp:
        case 0:
            print("Alerta: Punto de Congelación")
        case 100:
            print("Alerta: Punto de Ebullición")
        case _:
            # Operador ternario interno para evaluar el rango
            estado = "Estado: Estable" if 10 <= temp <= 30 else "Estado: Crítico"
            print(estado)
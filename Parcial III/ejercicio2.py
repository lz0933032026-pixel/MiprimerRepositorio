# Ejercicio 2: Terminal de cobro seguro con Decimal

from decimal import Decimal, InvalidOperation

total = Decimal("0")  # acumulador con precisión real

while True:
    precio = input("Ingrese el precio del producto (0 para finalizar): ")

    try:
        monto = Decimal(precio)  # convierte la entrada a Decimal

        if monto == 0:
            break  # cierra el sistema
        elif monto < 0:
            print("El precio no puede ser negativo.")
            continue

        total += monto  # acumula el monto
        print(f"Subtotal actual: ${total}")

    except InvalidOperation:  # captura errores de texto
        print("⚠️ Error: ingrese solo números válidos.")
        continue  # permite seguir sin cerrar el programa

print(f"💰 Total acumulado: ${total}") 
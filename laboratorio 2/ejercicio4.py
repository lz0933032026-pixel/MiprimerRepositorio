using, System;
using, System.Collections.Generic;
using ,System.Linq

namespace:MiAplicacion
{
    public static class TransformadorLista
    {
        // Función que recibe una lista de palabras y un número
        public static List<string> AplicarTransformacion(List<string> palabras, int opcion)
        {
            return palabras.Select(p =>
            {
                if (string.IsNullOrEmpty(p)) return "Texto vacío";

                return opcion switch
                {
                    1 => p.ToUpper(), // Mayúsculas
                    2 => p.ToLower(), // Minúsculas
                    3 => char.ToUpper(p[0]) + p.Substring(1).ToLower(), // Primera letra en mayúscula
                    _ => "Opción inválida"
                };
            }).ToList();
        }
    }

    class Program
    {
        static void Main()
        {
            Console.WriteLine("=== Ejercicio 4 ===");
            Console.Write("Ingrese varias palabras separadas por espacio: ");
            var listaPalabras = Console.ReadLine().Split(' ').ToList();

            Console.WriteLine("\nOpciones: 1 = MAYÚSCULAS, 2 = minúsculas, 3 = Primera letra");
            Console.Write("Ingrese el número de opción: ");

            if (int.TryParse(Console.ReadLine(), out int opcion))
            {
                var resultado = TransformadorLista.AplicarTransformacion(listaPalabras, opcion);
                Console.WriteLine("\nResultado:\n" + string.Join("\n", resultado));
            }
            else
            {
                Console.WriteLine("\nDebe ingresar un número válido.");
            }
        }
    }
}
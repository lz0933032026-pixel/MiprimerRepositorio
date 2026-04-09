using ,System;

namespace :MiAplicacion
{
    class Program
    {
        // Función que transforma el texto y devuelve la cantidad de caracteres
        static int TransformarYContar(string texto, int opcion)
        {
            if (string.IsNullOrEmpty(texto)) return 0;

            string resultado = opcion switch
            {
                1 => texto.ToUpper(), // Mayúsculas
                2 => texto.ToLower(), // Minúsculas
                3 => char.ToUpper(texto[0]) + texto.Substring(1).ToLower(), // Primera letra en mayúscula
                _ => "Opción inválida"
            };

            return resultado.Length;
        }

        static void Main()
        {
            Console.WriteLine("=== Ejercicio 6 ===");
            Console.Write("Ingrese un texto: ");
            string texto = Console.ReadLine();

            Console.Write("Ingrese una opción (1, 2 o 3): ");
            if (int.TryParse(Console.ReadLine(), out int opcion))
            {
                int cantidad = TransformarYContar(texto, opcion);
                Console.WriteLine($"\nCantidad de caracteres del resultado: {cantidad}");
            }
            else
            {
                Console.WriteLine("\nDebe ingresar un número válido.");
            }
        }
    }
}
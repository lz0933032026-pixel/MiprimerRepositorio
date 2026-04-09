using ,System;

namespace :MiAplicacion
{
    class Program
    {
        // Función que aplica la transformación según la opción
        static string Transformar(string texto, int opcion)
        {
            if (string.IsNullOrEmpty(texto)) return "Texto vacío";

            return opcion switch
            {
                1 => texto.ToUpper(), // Mayúsculas
                2 => texto.ToLower(), // Minúsculas
                3 => char.ToUpper(texto[0]) + texto.Substring(1).ToLower(), // Primera letra en mayúscula
                _ => "Opción inválida"
            };
        }

        static void Main()
        {
            Console.WriteLine("=== Ejercicio 8 ===");
            Console.Write("Ingrese un texto: ");
            string texto = Console.ReadLine();

            Console.WriteLine("\nMenú de opciones:");
            Console.WriteLine("1 = Convertir a MAYÚSCULAS");
            Console.WriteLine("2 = Convertir a minúsculas");
            Console.WriteLine("3 = Primera letra en mayúscula");

            Console.Write("\nSeleccione una opción: ");
            if (int.TryParse(Console.ReadLine(), out int opcion))
            {
                string resultado = Transformar(texto, opcion);
                Console.WriteLine("\nResultado: " + resultado);
            }
            else
            {
                Console.WriteLine("\nDebe ingresar un número válido.");
            }

            Console.WriteLine("\nPrograma finalizado.");
        }
    }
}
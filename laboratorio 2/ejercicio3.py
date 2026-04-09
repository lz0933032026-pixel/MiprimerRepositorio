using  ,System 
using ,System: Collections.Generic;
namespace :MiAplicacion
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Ejercicio 3 ===");
            Console.WriteLine("Este programa solicita un texto y un número para aplicar una transformación.\n");

            // Solicitar texto
            Console.Write("Ingrese un texto: ");
            string texto = Console.ReadLine();

            // Definir transformaciones en un diccionario
            var transformaciones = new Dictionary<int, Func<string, string>>
            {
                { 1, t => t.ToUpper() }, // Mayúsculas
                { 2, t => t.ToLower() }, // Minúsculas
                { 3, t => string.IsNullOrEmpty(t) ? t : char.ToUpper(t[0]) + t.Substring(1).ToLower() } // Primera letra en mayúscula
            };

            // Solicitar opción
            Console.WriteLine("\nSeleccione una opción:");
            Console.WriteLine("1 = Convertir a MAYÚSCULAS");
            Console.WriteLine("2 = Convertir a minúsculas");
            Console.WriteLine("3 = Primera letra en mayúscula");

            Console.Write("Ingrese el número de opción: ");
            if (int.TryParse(Console.ReadLine(), out int opcion))
            {
                if (transformaciones.ContainsKey(opcion))
                {
                    string resultado = transformaciones[opcion](texto);
                    Console.WriteLine("\nResultado: " + resultado);
                }
                else
                {
                    Console.WriteLine("\nOpción inválida.");
                }
            }
            else
            {
                Console.WriteLine("\nDebe ingresar un número válido.");
            }

            Console.WriteLine("\nPrograma finalizado.");
        }
    }
}
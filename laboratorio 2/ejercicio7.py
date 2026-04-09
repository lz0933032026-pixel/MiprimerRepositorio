using ,System;
using ,System.Collections.Generic;

namespace :  MiAplicacion
{
    class Program
    {
        // Función que aplica cada transformación en orden
        static string TransformarSecuencia(string texto, List<int> opciones)
        {
            if (string.IsNullOrEmpty(texto)) return "Texto vacío";

            foreach (int opcion in opciones)
            {
                texto = opcion switch
                {
                    1 => texto.ToUpper(), // Mayúsculas
                    2 => texto.ToLower(), // Minúsculas
                    3 => char.ToUpper(texto[0]) + texto.Substring(1).ToLower(), // Primera letra en mayúscula
                    _ => "Opción inválida"
                };
            }

            return texto;
        }

        static void Main()
        {
            Console.WriteLine("=== Ejercicio 7 ===");
            Console.Write("Ingrese un texto: ");
            string texto = Console.ReadLine();

            Console.WriteLine("\nIngrese una lista de números (1, 2 o 3) separados por espacio:");
            string entrada = Console.ReadLine();
            List<int> opciones = new List<int>();

            foreach (string num in entrada.Split(' '))
                if (int.TryParse(num, out int valor))
                    opciones.Add(valor);

            string resultado = TransformarSecuencia(texto, opciones);
            Console.WriteLine("\nResultado final: " + resultado);
        }
    }
}
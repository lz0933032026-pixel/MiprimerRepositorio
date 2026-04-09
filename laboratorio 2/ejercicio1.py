 {
         // Función que transforma el texto según la opción
        static string TransformarTexto(string texto, int opcion)
        {
            switch (opcion)
            {
                case 1:
                    return texto.ToUpper(); // Mayúsculas
                case 2:
              using System;

namespace : MiAplicacion
{ 
    class Program      return texto.ToLower(); // Minúsculas
                case 3:
                    if (string.IsNullOrEmpty(texto))
                        return texto;
                    return char.ToUpper(texto[0]) + texto.Substring(1).ToLower(); // Primera letra mayúscula
                default:
                    return "Opción inválida.";
            }
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Ingrese un texto:");
            string texto = Console.ReadLine();

            Console.WriteLine("Seleccione una opción:");
            Console.WriteLine("1 = Convertir a MAYÚSCULAS");
            Console.WriteLine("2 = Convertir a minúsculas");
            Console.WriteLine("3 = Primera letra en mayúscula");

            int opcion;
            if (int.TryParse(Console.ReadLine(), out opcion))
            {
                string resultado = TransformarTexto(texto, opcion);
                Console.WriteLine("Resultado: " + resultado);
            }
            else
            {
                Console.WriteLine("Debe ingresar un número válido.");
            }
        }
    }
} 
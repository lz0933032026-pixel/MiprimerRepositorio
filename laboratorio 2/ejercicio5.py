using, System;

namespace : MiAplicacion
{
    class , Program
    {
        static string Transformar(string texto, int opcion)
        {
            return opcion switch
            {
                1 => texto.ToUpper(),
                2 => texto.ToLower(),
                3 => char.ToUpper(texto[0]) + texto.Substring(1).ToLower(),
                _ => "Opción inválida"
            };
        }

        static void Main()
        {
            Console.Write("Ingrese un texto: ");
            string texto = Console.ReadLine();

            Console.Write("Ingrese una opción (1, 2 o 3): ");
            if (int.TryParse(Console.ReadLine(), out int opcion))
                Console.WriteLine("Resultado: " + Transformar(texto, opcion));
            else
                Console.WriteLine("Debe ingresar un número válido.");
        }
    }
}
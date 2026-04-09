using : System 

namespace : MiAplicacion
{
    class  Program
    {
        // Función que recibe una palabra y un número
        static string TransformarPalabra(string palabra, int opcion)
        {
            switch (opcion)
            {
                case 1:
                    return palabra.ToUpper(); // Mayúsculas
                case 2:
                    return palabra.ToLower(); // Minúsculas
                case 3:
                    if (string.IsNullOrEmpty(palabra))
                        return palabra;
                    return char.ToUpper(palabra[0]) + palabra.Substring(1).ToLower(); // Primera letra mayúscula
                default:
                    return "Opción inválida.";
            }
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Ingrese una palabra:");
            string palabra = Console.ReadLine();

            Console.WriteLine("Seleccione una opción:");
            Console.WriteLine("1 = Convertir a MAYÚSCULAS");
            Console.WriteLine("2 = Convertir a minúsculas");
            Console.WriteLine("3 = Primera letra en mayúscula");

            int opcion;
            if (int.TryParse(Console.ReadLine(), out opcion))
            {
                string resultado = TransformarPalabra(palabra, opcion);
                Console.WriteLine("Resultado: " + resultado);
            }
            else
            {
                Console.WriteLine("Debe ingresar un número válido.");
            }
        }
    }
}
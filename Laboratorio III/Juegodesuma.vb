Module JuegoDeSuma
    Sub Main()
        Dim nivel, num1, num2, respuesta, resultado, puntaje As Integer
        Dim continuar As String = "S"

        ' Inicializar generador de números aleatorios
        Randomize()

        Console.WriteLine("=== JUEGO DE SUMA ===")
        Console.WriteLine("1. Fácil  2. Medio  3. Difícil")
        Console.Write("Elige nivel: ")
        nivel = CInt(Console.ReadLine())

        Select Case nivel
            Case 1
                Console.WriteLine("Nivel FÁCIL seleccionado.")
            Case 2
                Console.WriteLine("Nivel MEDIO seleccionado.")
            Case 3
                Console.WriteLine("Nivel DIFÍCIL seleccionado.")
            Case Else
                Console.WriteLine("Nivel inválido, se usará FÁCIL.")
                nivel = 1
        End Select

        ' Ciclo principal del juego
        While continuar.ToUpper() = "S"
            For i = 1 To 3
                Select Case nivel
                    Case 1
                        num1 = CInt(Int((10 * Rnd()) + 1))
                        num2 = CInt(Int((10 * Rnd()) + 1))
                    Case 2
                        num1 = CInt(Int((50 * Rnd()) + 1))
                        num2 = CInt(Int((50 * Rnd()) + 1))
                    Case 3
                        num1 = CInt(Int((100 * Rnd()) + 1))
                        num2 = CInt(Int((100 * Rnd()) + 1))
                End Select

                Console.WriteLine()
                Console.WriteLine($"{num1} + {num2} = ?")
                Console.Write("Tu respuesta: ")
                respuesta = CInt(Console.ReadLine())
                resultado = num1 + num2

                If respuesta = resultado Then
                    puntaje += 10
                    Console.WriteLine("¡Correcto! Puntaje actual: " & puntaje)
                Else
                    Console.WriteLine("Incorrecto. La respuesta era: " & resultado)
                End If
            Next

            Console.WriteLine()
            Console.Write("¿Deseas continuar jugando? (S/N): ")
            continuar = Console.ReadLine()
        End While

        Console.WriteLine()
        Console.WriteLine($"Juego terminado. Puntaje final: {puntaje}")
        Console.WriteLine("Gracias por jugar el Juego de Suma.")
        Console.ReadKey()
    End Sub
End Module